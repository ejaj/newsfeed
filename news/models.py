from django.db import models


# Create your models here.


class Sources(models.Model):
    """
    Create Model Class for Sources
    """
    newsap_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'sources'


class News(models.Model):
    """
    Create Model Class for News
    """
    source_id = models.CharField(max_length=200, null=True, blank=True)
    source_name = models.CharField(max_length=200, null=True, blank=True)
    source_url = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=10, null=True)
    category = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    urlToImage = models.CharField(max_length=200, null=True, blank=True)
    publishedAt = models.DateTimeField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news'


class NewsNotification(models.Model):
    """
     Create Model Class for NewsNotification
    """
    news_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news_notification'
