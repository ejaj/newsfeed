# Generated by Django 2.2.7 on 2021-03-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210320_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='source_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
