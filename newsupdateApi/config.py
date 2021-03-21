from newsapi import NewsApiClient

def news_client():
    """
    Pass api key into NewsApiClient Class.
    :return:
    """
    client = NewsApiClient(api_key='530fb6f957a148cd8c7655d5e8209a24')
    return client