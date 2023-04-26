import feedparser
import requests
import html2text
from bs4 import BeautifulSoup

# RSSのURL
rss_url = "https://feeds.feedburner.com/TheHackersNews"

# RSSからニュースを取得する
def get_news():
    list_html = extract_link_from_rss(rss_url)
    extract_text_from_html(list_html)


# RSSからlinkタグのURLを取得する
def extract_link_from_rss(rss_url) -> list:
    rss = feedparser.parse(rss_url)
    link_list = [entry.link for entry in rss.entries]
    return link_list

# リストのHTMLからテキストを抽出する
def extract_text_from_html(list_html) -> list:
    html = list_html[0]
    print("#############", html)
    response = requests.get(html)
    
    if response.status_code == 200:
        html_parse(response.text)
    else:
        print(f"Error fetching content from {html}, status code: {response.status_code}")

# BeautifulsoupさんにHTML投げてclass指定して本文を拾ってもらう
def html_parse(html_link):
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