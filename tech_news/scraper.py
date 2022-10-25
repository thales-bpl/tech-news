import requests
import time
from parsel import Selector
from tech_news.database import create_news


def responseCheck(response):
    return response.text if response.status_code == 200 else None


# Requisito 1
def fetch(url):
    try:
        header = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=header, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError,
            requests.Timeout,
            requests.ConnectionError) as error:
        print(error)
        return None
    return responseCheck(response)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_list = []
    news_list = selector.css(".entry-title a::attr(href)").getall()
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".next::attr(href)").get()
    return next_page_url if next_page_url else None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_data = {
        "url": selector.css("head link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": len(selector.css("ol.comment-list li").getall()),
        "summary": "".join(selector.css(
            ".entry-content > p:nth-of-type(1) *::text"
        ).getall()).strip(),
        "tags": selector.css("section.post-tags a::text").getall(),
        "category": selector.css("a.category-style span.label::text").get(),
    }
    return news_data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news_to_be_added = []

    while len(news_to_be_added) < amount:
        page_html_content = fetch(url)
        news_url_list = scrape_novidades(page_html_content)
        for news_url in news_url_list:
            if len(news_to_be_added) < amount:
                news_html = fetch(news_url)
                news_to_be_added.append(scrape_noticia(news_html))
        url = scrape_next_page_link(page_html_content)

    create_news(news_to_be_added)
    return news_to_be_added
