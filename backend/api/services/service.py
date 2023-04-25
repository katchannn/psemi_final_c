import feedparser
import requests
import html2text

# RSSのURL
rss_url = "https://feeds.feedburner.com/TheHackersNews"
h = html2text.HTML2Text()
h.ignore_links = True
h.escape_all = True

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
        print(h.handle(response.text))
    else:
        print(f"Error fetching content from {html}, status code: {response.status_code}")