# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-11-13 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='record_stat',
            field=models.CharField(default='O', max_length=1),
        ),
    ]
