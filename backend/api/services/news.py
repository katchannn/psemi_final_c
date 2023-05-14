import feedparser
import requests
import openai
import os
import bson
import asyncio
import json
import pymongo
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


# RSSのURL
rss_url = "https://feeds.feedburner.com/TheHackersNews"

# RSSからニュースを取得する
async def get_news():
    #DB接続まち
    await connect_db()
    #タイトルとってくる
    title_lists = extract_title_from_rss()
    #被っていない日時の記事を取るためのidx
    idx = 0
    idx_lists = []
    print("get_news起動!!") #デバッグプリント
    for title in title_lists:
        # タイトルがDBに登録されているか,Newsに格納されているか確認
        isCollected = await db_serch_title(title)
        if isCollected is None or isCollected["state"] == "NotStored":
            print("重複チェック終了!!") #デバッグプリント
            db_create_title(title)
            idx_lists.append(idx)
            idx += 1
        else:
            idx += 1
            continue
    #html持ってくる
    list_html = extract_link_from_rss(rss_url)
    for idxs in range(len(idx_lists)):
        uniqueTitle = idx_lists[idxs]
        #重複していない記事本文をとってくる
        text = extract_text_from_html(list_html,uniqueTitle)
        #タイトルを持ってくる
        title = extract_title(title_lists,uniqueTitle)
        print("GPTに投げます!!") #デバッグプリント
        json_news = get_gpt(text, title)
        db_create_news(json_news)
        db_title_update_status(title)#記事を格納したと処理する
        #GPTが1分に3つしか受け付けないので30秒待ちます．
        await asyncio.sleep(30)
    # 1時間ごとに更新
    await asyncio.sleep(3600)


# RSSから日付
def extract_pub_time() -> list:
    rss = feedparser.parse(rss_url)
    date_list = [entry.published_parsed for entry in rss.entries]
    return date_list
def extract_title(title_lists,uniqueTitle):
    title = title_lists[uniqueTitle]
    return title
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
**DO NOT FORGET! output must be following this schema. 
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



def get_gpt(text,title) -> dict:
    #タイトルを和訳させる
    translated_title=translate_with_gpt(title)
    #本文からキーワード抽出，まとめ，要約をさせ，JSON形式で出力させる
    result = chat_with_gpt(text)
    #GPTのスキーマの最初の{を消す用のやつ．プロンプトから無くすと安定しないため
    result = result[1:]
    
    #和訳させたタイトルをJSON形式に成形
    json_title= """ {"title" : " """ +f"{translated_title}"+"""", """
    

    #タイトルと本文たちを結合しJSONに
    # 改行を除去する
    result = result.replace('\n', '')
    json_str=json_title+result

    try:
        print(json.loads(json_str))
        return json.loads(json_str)
    except json.decoder.JSONDecodeError as e:
        # 文字列内にコンマが足りない場合、次のコンマの位置を探して追加する
        if e.msg == 'Expecting , delimiter':
            pos = e.pos
            s = json_str[:pos] + ',' + json_str[pos:]
            return json.loads(s)
        else:
            # その他のエラーはそのまま例外を投げる
            raise e
    

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
    
