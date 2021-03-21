from django.http import HttpResponse
from django.shortcuts import render
from .models import News
from accounts.models import UserNewsSetting
from newsupdateApi.newsApi import update_news
from newsupdateApi.sources import update_sources
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F


# Create your views here.


def index(request):
    """
    Check user logged in, if logged in then getting news base on user preference, if user not logged in
    then getting all news from model:News
    Get logged user preference from model:UserNewsSetting
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        try:

            news_setting = UserNewsSetting.objects.get(user_id=request.user.id)

            countries = news_setting.countries
            countries_list = list(countries.split(","))
            news_source = news_setting.news_source
            news_source_list = list(news_source.split(","))

            top_headlines = News.objects.filter(
                Q(country__in=countries_list) |
                Q(source_name__in=news_source_list)
            ).order_by('-publishedAt')
            if top_headlines:
                top_headlines = top_headlines
            else:
                top_headlines = News.objects.all().order_by('-publishedAt')
        except ObjectDoesNotExist:
            top_headlines = News.objects.all().order_by('-publishedAt')
    else:
        top_headlines = News.objects.all().order_by('-publishedAt')

    page = request.GET.get('page', 1)

    paginator = Paginator(top_headlines, 10)

    try:
        top_headlines = paginator.page(page)
    except PageNotAnInteger:
        top_headlines = paginator.page(1)
    except EmptyPage:
        top_headlines = paginator.page(paginator.num_pages)

    return render(request, 'index.html', context={"top_headings": top_headlines})


def initial_news_api(request):
    """
    initially news fetch.
    :param request:
    :return:
    """
    update_sources()
    update_news()
    return HttpResponse("initially news fetch")
