# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0019_auto_20171019_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chaxun1',
            options={'verbose_name': '征信查询-机构', 'verbose_name_plural': '征信查询-机构'},
        ),
        migrations.AlterModelOptions(
            name='chaxun2',
            options={'verbose_name': '征信查询-个人', 'verbose_name_plural': '征信查询-个人'},
        ),
        migrations.AlterField(
            model_name='chaxun1',
            name='reason',
            field=models.CharField(choices=[('贷后管理', '贷后管理'), ('信用卡审批', '信用卡审批'), ('贷款审批', '贷款审批'), ('保前审查', '保前审查'), ('担保资格审查', '担保资格审查'), ('特约商户实名审查', '特约商户实名审查'), ('其他', '其他')], max_length=20, verbose_name='查询原因'),
        ),
    ]
