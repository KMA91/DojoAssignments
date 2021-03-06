# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0006_auto_20170421_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='secrets.Message'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='secrets.Users'),
        ),
    ]
