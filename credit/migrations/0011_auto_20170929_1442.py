# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0010_luresult_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='luresult',
            name='order',
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': '信用卡信息（最多添加20条）', 'verbose_name_plural': '信用卡信息（最多添加20条）'},
        ),
        migrations.AlterModelOptions(
            name='loan',
            options={'verbose_name': '贷款信息（最多添加20条）', 'verbose_name_plural': '贷款信息（最多添加20条）'},
        ),
        migrations.AddField(
            model_name='basic',
            name='luru',
            field=models.BooleanField(default=False, verbose_name='录入完成'),
        ),
        migrations.AddField(
            model_name='basic',
            name='luruyuan',
            field=models.CharField(default='', max_length=15, null=True, verbose_name='录入员'),
        ),
        migrations.DeleteModel(
            name='luresult',
        ),
    ]