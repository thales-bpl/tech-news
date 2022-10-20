import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
