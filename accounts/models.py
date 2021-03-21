from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class UserNewsSetting(models.Model):
    """
    Create Model Class for UserNewsSetting.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    countries = models.CharField(max_length=200, null=True, blank=True)
    news_source = models.CharField(max_length=200, null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'user_news_setting'


class Profile(models.Model):
    """
    Create Model Class for User Profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'user_profile'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """
    Create profile by post_save signal, date insert to model:Profile while user sign up.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create user token for API authentication by post_save signal while user sign up.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Token.objects.create(user=instance)
