import feedparser
import requests
import openai
import os
import json
from bs4 import BeautifulSoup
from cruds.news import *

#openAIキー
variable1 = os.environ.get('OPENAI_API_KEY')
openai.api_key = variable1

#mongoDBのやつ
#env
HOST = 'mongo'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

#connect to mongodb
DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
client = MongoClient(DATABASE_URL)


# RSSのURL
rss_url = "https://feeds.feedburner.com/TheHackersNews"

# RSSからニュースを取得する
def get_news() -> str:
    #被っていない日時の記事を取るためのidx
    idx=0
    idx_lists=[]
    print("get_news起動!!") #デバッグプリント
    #ニュースの公開日をとってくる
    list_time = extract_pub_time()
    for time in list_time:
        # 日時がDBに登録されているか確認
        isCollected = db_serch_time(time)
        if isCollected is not None:
            print("時間関係起動!!") #デバッグプリント
            db_create_time(time)
            idx_lists.append(idx)
            idx+=1
        else:
            idx+=1
            continue
    #html持ってくる
    list_html = extract_link_from_rss(rss_url)
    #タイトルとってくる
    title_lists = extract_title_from_rss()
    for idxs in idx_lists:
        uniqueTitle = idx_lists[idxs]
        #重複していない記事本文をとってくる
        text = extract_text_from_html(list_html,uniqueTitle)
        #タイトルを持ってくる
        title = extract_title_from_rss(title_lists,uniqueTitle)
        json=get_gpt(text,title)
        db_create_news(json)
    

# RSSから日付
def extract_pub_time() -> list:
    rss = feedparser.parse(rss_url)
    date_list = [entry.published_parsed for entry in rss.entries]
    return date_list

# RSSからタイトルを取得する
def extract_title_from_rss() -> list:
    rss = feedparser.parse(rss_url)
    title_list = [entry.title for entry in rss.entries]
    return title_list

# RSSからlinkタグのURLを取得する
def extract_link_from_rss(rss_url) -> list:
    rss = feedparser.parse(rss_url)
    link_list = [entry.link for entry in rss.entries]
    return link_list

# リストのHTMLからテキストを抽出する
def extract_text_from_html(list_html,uniqueTitle) -> str:
    html = list_html[uniqueTitle]
    print("URL:", list)
    response = requests.get(html)
    
    if response.status_code == 200:
        return html_parse(response.text)
    else:
        print(f"Error fetching content from {html}, status code: {response.status_code}")

# BeautifulsoupさんにHTML投げてclass指定して本文を拾ってもらう
def html_parse(html_link) -> str:
    soup = BeautifulSoup(html_link, 'html.parser')
    for ad in soup.find_all('div', {'class': 'ad_two clear'}):
        ad.decompose()

    # 本文を含む要素を取得する
    article = soup.find('div', {'class': 'articlebody clear cf'})
    for cf in article.find_all('div', {'class': 'cf note-b'}):
        cf.decompose()

    # テキストを抽出する
    text = article.get_text()

    #  変換されたテキストを返す
    return text

#こっからchatGPT

prompt= """
Notes
・output must be extracted from the entire article that are important for cybersecurity.
・output must be following this schema.
・output must be following article.
・"keyword" must be in Japanese.
・output are read by student that are not familiar with the information technology. so that output should be kindly.
・"keyword" must be extract three And Important Words to understand the article.
・"keywords" should be extracted for cybersecurity novices in Japanese.
・"key" must be general knowledge.
・Please summarize clealy the entire article when output "content".
・"content" must be about 600 words in Japanese.
{
  "keywords": {
    "keyword 1 from article in 日本語": "description for keyword 1",
    "keyword 2 from article in Japanese"": "description for keyword 2",
    "keyword 3 from article in Japanese": "description for keyword 3"
  },
  "content": "clealy summarized text about the entire article about 600 words in Japanese."
}


"""



def get_gpt(text,title) -> json:
    #タイトルを和訳させる
    translated_title=translate_with_gpt(title)
    #本文からキーワード抽出，まとめ，要約をさせ，JSON形式で出力させる
    result = chat_with_gpt(text)
    #和訳させたタイトルをJSON形式に成形
    json_title=""" {"title" : " """ +f"{translated_title}"+"""", """
    #タイトルと本文たちを結合しJSONに
    responses = json.dumps(json_title+result)
    #確認
    print(json.loads(responses))
    #JSONか判別
    try:
        json_data = json.loads(responses)
        print("This is a valid JSON.")
        return json_data
    except ValueError:
        print("This is not a valid JSON.")

def translate_with_gpt(title):
    completion = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are the AI that good at English and Japanese. And you are the AI that familiar with information technology."},
                  {"role":"user","content":f"Please translate into Japanese.\n{title}"}
    ])
    response = completion.choices[0].message.content
    return response

def chat_with_gpt(text):
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are the AI that good at cybersecurity,English and Japanese. And you are an AI that excels at text summarizing. "},
                  {"role":"system","content":"You are also familiar with the information technology."},
                  {"role":"user","content":"Please read this article. when you have read article, please output this schema. Please follow Notes."
                   +f"\narticle:{text}\n"+prompt
}]
    )
    
    response = completion.choices[0].message.content
    
    return response
    
