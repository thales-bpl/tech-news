from tech_news.database import find_news


# Requisito 10
def top_5_news():
    # src: https://www.educative.io
    # /answers/how-to-sort-a-list-of-tuples-in-python-using-lambda
    top_five_news = []
    all_news = find_news()
    sorted_news = sorted(
        all_news,
        key=lambda news: news['comments_count'],
        reverse=True
    )

    for news in sorted_news[:5]:
        top_five_news.append((news["title"], news["url"]))

    return top_five_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
