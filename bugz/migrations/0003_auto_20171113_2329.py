# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-11-13 14:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugz', '0002_auto_20171113_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
