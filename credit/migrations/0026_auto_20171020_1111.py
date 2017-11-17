# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0025_auto_20171019_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic',
            name='IDcard',
        ),
        migrations.AlterField(
            model_name='basic',
            name='order_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='进件编号'),
        ),
        migrations.AlterField(
            model_name='chaxun1',
            name='chaxun_date',
            field=models.DateField(null=True, verbose_name='查询日期'),
        ),
        migrations.AlterField(
            model_name='chaxun2',
            name='chaxun_date',
            field=models.DateField(null=True, verbose_name='查询日期'),
        ),
        migrations.AlterField(
            model_name='ggjl',
            name='public_record',
            field=models.TextField(blank=True, default='无', max_length=2000, verbose_name='公共记录'),
        ),
    ]