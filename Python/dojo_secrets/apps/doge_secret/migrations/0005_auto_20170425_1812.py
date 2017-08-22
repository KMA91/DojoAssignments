# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doge_secret', '0004_auto_20170421_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secret_likes', to='doge_secret.Posts'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='doge_secret.Users'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secrets_created', to='doge_secret.Users'),
        ),
    ]
