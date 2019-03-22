# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190220_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='third_app',
            field=models.SmallIntegerField(choices=[(0, 'Local user.'), (1, '科技云通行证')], default=0, verbose_name='第三方应用登录'),
        ),
    ]