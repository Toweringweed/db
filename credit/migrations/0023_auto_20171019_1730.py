# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0022_auto_20171019_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='luruyuan',
            field=models.CharField(default='', max_length=20, verbose_name='录入员'),
        ),
    ]
