# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_auto_20170928_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='yuqi_money',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='逾期金额'),
        ),
        migrations.AlterField(
            model_name='basic',
            name='name',
            field=models.CharField(default='', max_length=10, verbose_name='客户姓名'),
        ),
        migrations.AlterField(
            model_name='basic',
            name='order_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='订单流水号'),
        ),
        migrations.AlterField(
            model_name='basic',
            name='type',
            field=models.CharField(choices=[('jian', '简版征信'), ('xiang', '详版征信')], default='jian', max_length=6, verbose_name='征信类型'),
        ),
        migrations.AlterField(
            model_name='card',
            name='query_date',
            field=models.DateField(blank=True, null=True, verbose_name='截止日期'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='account_category',
            field=models.CharField(default='', max_length=10, verbose_name='贷款性质'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='grant_date',
            field=models.DateField(blank=True, null=True, verbose_name='发放日期'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='query_date',
            field=models.DateField(null=True, verbose_name='截止日期'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='type',
            field=models.CharField(choices=[('fang', '房贷'), ('other', '其他贷款')], default='---', max_length=6, verbose_name='贷款类型'),
        ),
    ]