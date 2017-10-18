# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datago', '0006_auto_20170828_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='repayment',
            name='repay_month',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='月还款额'),
        ),
        migrations.AlterField(
            model_name='order_t',
            name='contract_id',
            field=models.CharField(default='', max_length=30, primary_key=True, verbose_name='合同编号'),
        ),
        migrations.AlterField(
            model_name='order_t',
            name='department',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False, verbose_name='营业部名称'),
        ),
    ]
