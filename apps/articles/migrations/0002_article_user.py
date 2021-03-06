# Generated by Django 2.0.10 on 2019-01-31 13:28

import articles.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(articles.models.get_sentinel_user), to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
    ]
