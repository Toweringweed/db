# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20170928_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='type',
            field=models.CharField(choices=[('fang', '房贷'), ('other', '其他贷款')], default='---', max_length=10),
        ),
        migrations.AlterField(
            model_name='basic',
            name='adress',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='征信地址'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='query_date',
            field=models.DateField(null=True, verbose_name='截止年月'),
        ),
    ]