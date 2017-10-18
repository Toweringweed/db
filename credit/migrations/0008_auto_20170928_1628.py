# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0007_auto_20170928_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='summary',
            options={'verbose_name': '信用卡信息', 'verbose_name_plural': '信用卡信息'},
        ),
        migrations.AlterField(
            model_name='card',
            name='account_category',
            field=models.CharField(choices=[('贷记卡', '贷记卡'), ('信用卡', '信用卡'), ('准贷记卡', '准贷记卡')], max_length=10, verbose_name='卡类型'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_state',
            field=models.CharField(choices=[('持续中', '持续中'), ('已结清', '已结清')], max_length=10, verbose_name='贷款状态'),
        ),
    ]