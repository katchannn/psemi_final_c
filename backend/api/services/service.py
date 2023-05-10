import feedparser
import requests
import openai
import os
import json
from bs4 import BeautifulSoup

# RSSのURL
rss_url = "https://feeds.feedburner.com/TheHackersNews"

# RSSからニュースを取得する
def get_news() -> str:
    list_html = extract_link_from_rss(rss_url)
    pretext = extract_text_from_html(list_html)
    return html_parse(pretext)

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
def extract_text_from_html(list_html) -> list:
    html = list_html[0]
    print("URL:", html)
    response = requests.get(html)
    
    if response.status_code == 200:
        return response.text
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

    #  変換されたテキストを出力する
    print(text)
    return text



#記事ソース　https://thehackernews.com/2023/05/new-decoy-dog-malware-toolkit-uncovered.html
#ダミー記事(本文だけ).1記事あたり0.2ドルくらい?

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


variable1 = os.environ.get('OPENAI_API_KEY')
openai.api_key = variable1
def sample(text):
    #タイトルを持ってくる
    title_list=extract_title_from_rss()
    #タイトルを和訳させる
    translated_title=translate_with_gpt(title_list[0])
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
    except ValueError:
        print("This is not a valid JSON.")
    """
    以下抽出用 使わないかもだけど
    text = get_summary(responses)
    keywords = get_keyword(responses)
    print("text is:"+text)
    print("keywords is"+keywords)
    """

def translate_with_gpt(title):
    completion = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"You are the AI that good at English and Japanese. "},
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
    

"""
def get_summary(response_pyobj):
    
    responses=json.loads(response_pyobj)
    summary=responses["text"]
    return summary

def get_keyword(response_pyobj):
    responses=json.loads(response_pyobj)
    keywords=responses["keywords"]
    return keywords
"""
