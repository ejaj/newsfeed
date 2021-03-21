import datetime
import logging
from django.template.loader import render_to_string
from django.db.models import Q, F
from django.core.mail import BadHeaderError, send_mail

from .models import News, NewsNotification
from accounts.models import UserNewsSetting


def send_news_notification_to_user():
    """
    Send news to user base on his keywords
    Get user keywords from model:UserNewsSetting
    Get sent news id from model:NewsNotification for avoid repeating mail
    Get news from model:News base on today, keywords and sent news ids.

    :return:
    """
    today = datetime.date.today()
    news_ids = NewsNotification.objects.filter(created_at__gte=today).values_list('news_id', flat=True)
    for news_setting in UserNewsSetting.objects.annotate(email=F('user__email')).all():
        keywords = news_setting.keywords
        keywords_list = list(keywords.split(","))
        top_headlines = News.objects.filter(
            Q(category__in=keywords_list) & Q(created_at__gte=today)
        ).order_by('-publishedAt').exclude(id__in=news_ids)
        for headline in top_headlines:
            subject = headline.title
            email_template_name = "news_notification.txt"
            c = {
                "email": news_setting.email,
                "title": headline.title,
                "url": headline.url
            }
            template = render_to_string(email_template_name, c)
            try:
                send_mail(subject, template, 'kejaj.777@gmail.com', [news_setting.email], fail_silently=False)
                obj, created = NewsNotification.objects.get_or_create(
                    news_id=headline.id,
                    defaults={'news_id': headline.id},
                )
            except BadHeaderError:
                logging.error('Invalid header found.')


def delete_notification_news():
    """
    Delete all data from model:NewsNotification
    :return:
    """
    delete_notification = NewsNotification.objects.delete()
    return delete_notification
