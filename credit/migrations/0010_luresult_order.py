# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0009_auto_20170929_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='luresult',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='credit.basic'),
            preserve_default=False,
        ),
    ]
