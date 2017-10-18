# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0012_auto_20170929_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgurl', models.CharField(default='', max_length=100, null=True, verbose_name='图片地址')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.basic')),
            ],
            options={
                'verbose_name_plural': '征信影印图片',
                'verbose_name': '征信影印图片',
            },
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': '信用卡信息（最多添加30条, 不录非人民币账户）', 'verbose_name_plural': '信用卡信息（最多添加30条, 不录非人民币账户）'},
        ),
    ]