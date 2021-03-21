from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('user_news_feed/<int:user_id>', views.NewsFeedByUser.as_view(), name='user_news_feed'),
    path('get_api_token/', obtain_auth_token, name='get_api_token'),
]