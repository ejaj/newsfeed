from newsupdateApi.config import news_client
from news.models import News, Sources
from django.core.exceptions import ObjectDoesNotExist


def _get_news():
    """
    Get data from newsapi.org called everything news api.
    :return:
    """
    q = 'bitcoin'
    news_api = news_client()
    news_data = news_api.get_everything(q=q)
    articles = news_data['articles']
    return articles


def update_news():
    """
    Get source information data from model:Sources
    Api data store to model:News for further use.
    :return:
    """
    data = _get_news()
    if len(data) != 0:

        for i in range(len(data)):
            article = data[i]
            if article['source']['id']:

                try:
                    source_information = Sources.objects.get(
                        newsap_id=article['source']['id']
                    )
                    source_id = article['source']['id']
                    source_name = article['source']['name']
                    source_url = source_information.url
                    country = source_information.country
                    category = source_information.category
                    language = source_information.language
                except ObjectDoesNotExist:
                    source_id = None
                    source_name = article['source']['name']
                    source_url = None
                    country = None
                    category = None
                    language = None

            else:

                source_id = None
                source_name = article['source']['name']
                source_url = None
                country = None
                category = None
                language = None

            obj, created = News.objects.update_or_create(
                url=article['url'],
                defaults={
                    'source_id': source_id,
                    'source_name': source_name,
                    'source_url': source_url,
                    'country': country,
                    'category': category,
                    'language': language,
                    'title': article['title'],
                    'author': article['author'],
                    'description': article['description'],
                    'publishedAt': article['publishedAt'],
                    'urlToImage': article['urlToImage']

                },
            )
