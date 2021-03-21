# Generated by Django 2.2.7 on 2021-03-19 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNewsSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('news_source', models.CharField(blank=True, help_text='source of news must be coma separated', max_length=200, null=True)),
                ('keywords', models.CharField(blank=True, help_text='keyword must be coma separated', max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_news_setting', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_news_setting',
            },
        ),
    ]