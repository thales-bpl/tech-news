from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_found = []
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})

    for news in news_by_title:
        news_found.append((news["title"], news["url"]))

    return news_found


# Requisito 7
def search_by_date(date):
    try:
        news_found = []
        date = datetime.strptime(date, '%Y-%m-%d')
        date_db_format = datetime.strftime(date, '%d-%m-%Y')
        news_by_date = search_news({"timestamp": date_db_format})

        for news in news_by_date:
            news_found.append((news["title"], news["url"]))

    except ValueError:
        raise ValueError("Data inválida")

    return news_found


# Requisito 8
def search_by_tag(tag):
    news_found = []
    news_by_tag = search_news({"tags": {"$regex": tag, "$options": "i"}})

    for news in news_by_tag:
        news_found.append((news["title"], news["url"]))

    return news_found


# Requisito 9
def search_by_category(category):
    news_found = []
    news_by_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    for news in news_by_category:
        news_found.append((news["title"], news["url"]))

    return news_found
