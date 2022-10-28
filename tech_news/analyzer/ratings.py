from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():  # by comments_count
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
        top_five_news.append((news['title'], news['url']))

    return top_five_news


# Requisito 11
def top_5_categories():  # by news qt
    top_five_categories = []
    all_news = find_news()
    # src: https://www.digitalocean.com
    # /community/tutorials/python-counter-python-collections-counter
    # src2: https://stackoverflow.com/a/20872750/16499410
    # We'll use Counter() due to its O(n) complexility as opposed to
    # list.most_common() or list.count() as those would be O(n²)
    categories_counter = Counter(sorted(news['category'] for news in all_news))
    sorted_categories = categories_counter.most_common(5)  # O(n)

    for category in sorted_categories:
        top_five_categories.append(category[0])

    return top_five_categories
