# Generated by Django 2.2.7 on 2021-03-19 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usernewssetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernewssetting',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
