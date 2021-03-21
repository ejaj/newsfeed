from newsupdateApi.config import news_client
from news.models import Sources


def _get_sources():
    """
    Get data from newsapi.org called sources news api.
    :return:
    """
    news_api = news_client()
    sources = news_api.get_sources()
    sources_date = sources['sources']
    return sources_date


def update_sources():
    """
    Api data store to model:Sources for further use.
    :return:
    """
    data = _get_sources()
    if len(data) != 0:
        for i in range(len(data)):
            source = data[i]
            obj, created = Sources.objects.get_or_create(
                newsap_id=source['id'],
                category=source['category'],
                language=source['language'],
                country=source['country'],

                defaults={'name': source['name'], 'description': source['description'], 'url': source['url']},
            )
