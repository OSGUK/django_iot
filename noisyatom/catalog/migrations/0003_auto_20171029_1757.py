# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-29 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode', '0002_auto_20171029_1757'),
        ('catalog', '0002_auto_20170406_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='two_d_bar_code',
            field=models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='qrcode.QRcode'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='two_d_bar_code',
            field=models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='qrcode.QRcode'),
        ),
    ]
