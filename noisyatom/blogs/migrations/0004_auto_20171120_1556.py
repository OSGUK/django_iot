# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-20 15:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20171101_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 11, 20, 15, 56, 34, 54660, tzinfo=utc)),
        ),
    ]
