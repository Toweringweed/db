# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-23 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datago', '0002_auto_20170823_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract_t',
            name='product_class',
        ),
        migrations.RemoveField(
            model_name='order_t',
            name='product_class',
        ),
        migrations.AddField(
            model_name='contract_t',
            name='contract_date',
            field=models.DateField(blank=True, null=True, verbose_name='签约日期'),
        ),
        migrations.AddField(
            model_name='contract_t',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datago.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract_t',
            name='date_fangkuan',
            field=models.DateField(blank=True, null=True, verbose_name='放款日期'),
        ),
        migrations.AlterField(
            model_name='contract_t',
            name='date_shencha',
            field=models.DateField(blank=True, null=True, verbose_name='放款审查日期'),
        ),
        migrations.DeleteModel(
            name='product_class',
        ),
    ]
