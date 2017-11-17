# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0030_auto_20171103_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guarantee',
            options={'verbose_name': '担保信息（最多添加20条）', 'verbose_name_plural': '担保信息（最多添加20条）'},
        ),
        migrations.AddField(
            model_name='loan',
            name='account_category_main',
            field=models.CharField(blank=True, choices=[('个人住房贷款', '个人住房贷款'), ('个人公积金住房贷款', '个人公积金住房贷款'), ('个人消费贷款', '个人消费贷款'), ('个人经营贷款', '个人经营贷款'), ('个人信用贷款', '个人信用贷款'), ('农户贷款', '农户贷款'), ('个人汽车贷款', '个人汽车贷款'), ('住房抵押贷款', '住房抵押贷款'), ('汽车抵押贷款', '汽车抵押贷款'), ('抵押担保贷款', '抵押担保贷款'), ('其他抵押贷款', '其他抵押贷款'), ('装修贷款', '装修贷款'), ('助学贷款', '助学贷款'), ('其他贷款', '其他贷款')], max_length=30, verbose_name='贷款用途'),
        ),
        migrations.AlterField(
            model_name='chaxun1',
            name='reason',
            field=models.CharField(choices=[('贷后管理', '贷后管理'), ('信用卡审批', '信用卡审批'), ('贷款审批', '贷款审批'), ('担保资格审查', '担保资格审查'), ('特约商户实名审查', '特约商户实名审查'), ('保前审查', '保前审查'), ('保后管理', '保后管理'), ('准入资格审查', '准入资格审查'), ('其他', '其他')], max_length=20, verbose_name='查询原因'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='account_category',
            field=models.CharField(blank=True, default='', help_text='如果贷款用途选了其他贷款，请填写此项，否则无需填写', max_length=40, verbose_name='贷款用途(其他)'),
        ),
    ]