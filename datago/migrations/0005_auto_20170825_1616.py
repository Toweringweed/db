# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-25 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datago', '0004_auto_20170824_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repayment',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='last_date',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='over_days',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='overdue_settle',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='product',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='repay_part',
        ),
        migrations.RemoveField(
            model_name='repayment',
            name='repay_preact',
        ),
        migrations.AddField(
            model_name='repay',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='最后还款日期'),
        ),
        migrations.AddField(
            model_name='repay',
            name='over_days',
            field=models.IntegerField(blank=True, null=True, verbose_name='逾期天数'),
        ),
        migrations.AddField(
            model_name='repayment',
            name='contract_id',
            field=models.CharField(default='', max_length=40, verbose_name='合同编号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repayment',
            name='product_month',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datago.product_month'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repayment',
            name='residual_money2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12, verbose_name='计算期初剩余本金）'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repayment',
            name='yuqi_qici',
            field=models.IntegerField(default=0, verbose_name='累计逾期期次'),
        ),
        migrations.AlterField(
            model_name='repayment',
            name='repay_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='报表日期'),
        ),
    ]