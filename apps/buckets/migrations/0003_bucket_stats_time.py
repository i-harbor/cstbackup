# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0002_auto_20190225_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='stats_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='统计时间'),
        ),
    ]
