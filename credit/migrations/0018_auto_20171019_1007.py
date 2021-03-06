# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0017_auto_20171011_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='ggjl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_record', models.TextField(blank=True, default='无', verbose_name='公共记录')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.basic')),
            ],
            options={
                'verbose_name': '公共记录',
                'verbose_name_plural': '公共记录',
            },
        ),
        migrations.AlterField(
            model_name='chaxun1',
            name='reason',
            field=models.CharField(choices=[('贷后管理', '贷后管理'), ('信用卡审批', '信用卡审批'), ('贷款审批', '贷款审批'), ('保前审查', '保前审查'), ('特约商户实名审查', '特约商户实名审查'), ('其他', '其他')], max_length=20, verbose_name='查询原因'),
        ),
    ]
