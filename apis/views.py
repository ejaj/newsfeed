from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from news.models import News
from accounts.models import UserNewsSetting
from django.db.models import Q


class NewsFeedByUser(APIView):
    """
    NewsFeedByUser Class
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Check authentication user base on TOKEN
        Get news base on user preference.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = self.kwargs['user_id']

        news_setting = UserNewsSetting.objects.get(user_id=user_id)

        countries = news_setting.countries
        countries_list = list(countries.split(","))
        news_source = news_setting.news_source
        news_source_list = list(news_source.split(","))

        top_headlines = News.objects.filter(
            Q(country__in=countries_list) |
            Q(source_name__in=news_source_list)
        ).order_by('-publishedAt')

        data = {"top_headlines": list(
            top_headlines.values("title", "source_id", "source_name", "author", "url", "urlToImage", "description",
                                 "publishedAt"))}
        return Response(data)
