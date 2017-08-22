# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]