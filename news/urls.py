from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('initial_news_api', views.initial_news_api, name="initial_news_api"),
]
