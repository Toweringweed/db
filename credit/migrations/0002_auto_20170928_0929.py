# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_date', models.DateField(blank=True, null=True, verbose_name='查询年月')),
                ('card_account', models.IntegerField(null=True, verbose_name='信用卡账户数')),
                ('card_notsettled', models.IntegerField(null=True, verbose_name='信用卡未结清/未销户账户数')),
                ('card_overdue', models.IntegerField(null=True, verbose_name='信用卡发生过逾期的账户数')),
                ('card_90overdue', models.IntegerField(null=True, verbose_name='信用卡发生过90天以上逾期的账户数')),
                ('card_guaranty', models.IntegerField(null=True, verbose_name='信用卡为他人担保笔数')),
                ('housing_loan_account', models.IntegerField(null=True, verbose_name='购房贷款账户数')),
                ('housing_loan_notsettled', models.IntegerField(null=True, verbose_name='购房贷款未结清/未销户账户数')),
                ('housing_loan_overdue', models.IntegerField(null=True, verbose_name='购房贷款发生过逾期的账户数')),
                ('housing_loan_90overdue', models.IntegerField(null=True, verbose_name='购房贷款发生过90天以上逾期的账户数')),
                ('housing_loan_guaranty', models.IntegerField(null=True, verbose_name='购房贷款为他人担保笔数')),
                ('other_loan_account', models.IntegerField(null=True, verbose_name='其他贷款账户数')),
                ('other_loan_notsettled', models.IntegerField(null=True, verbose_name='其他贷款未结清/未销户账户数')),
                ('other_loan_overdue', models.IntegerField(null=True, verbose_name='其他贷款发生过逾期的账户数')),
                ('other_loan_90overdue', models.IntegerField(null=True, verbose_name='其他贷款发生过90天以上逾期的账户数')),
                ('other_loan_guaranty', models.IntegerField(null=True, verbose_name='其他贷款为他人担保笔数')),
            ],
        ),
        migrations.AddField(
            model_name='basic',
            name='adress',
            field=models.CharField(default='', max_length=200, verbose_name='征信地址'),
        ),
        migrations.AddField(
            model_name='basic',
            name='luru',
            field=models.BooleanField(default=False, verbose_name='录入是否完成'),
        ),
        migrations.AddField(
            model_name='basic',
            name='type',
            field=models.CharField(choices=[('jian', '简版征信'), ('xiang', '详版征信')], default='jian', max_length=10),
        ),
        migrations.AlterField(
            model_name='basic',
            name='IDcard',
            field=models.CharField(default='', max_length=19, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='card',
            name='credit_Line',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='信用额度'),
        ),
        migrations.AlterField(
            model_name='card',
            name='five_years_overdue',
            field=models.IntegerField(null=True, verbose_name='近五年内逾期月数'),
        ),
        migrations.AlterField(
            model_name='card',
            name='ninety_days_overdue',
            field=models.IntegerField(null=True, verbose_name='90天以上逾期次数'),
        ),
        migrations.AlterField(
            model_name='card',
            name='used_line',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='已使用额度'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c180_institution',
            field=models.IntegerField(null=True, verbose_name='近6个月机构查询次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c180_manage',
            field=models.IntegerField(null=True, verbose_name='近6个月贷后管理次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c180_personal',
            field=models.IntegerField(null=True, verbose_name='近6个月个人查询次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c30_institution_query',
            field=models.IntegerField(null=True, verbose_name='近30天机构查询次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c30_manage',
            field=models.IntegerField(null=True, verbose_name='近30天贷后管理次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c30_person',
            field=models.IntegerField(null=True, verbose_name='近30天个人查询次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c60_institution',
            field=models.IntegerField(null=True, verbose_name='近2个月机构查询次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c60_manage',
            field=models.IntegerField(null=True, verbose_name='近2个月贷后管理次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c60_personal',
            field=models.IntegerField(null=True, verbose_name='近2个月个人查询次数'),
        ),
        migrations.AlterField(
            model_name='chaxun',
            name='c_date',
            field=models.DateField(null=True, verbose_name='查询年月'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='days90_overdue',
            field=models.IntegerField(null=True, verbose_name='90天以上逾期次数'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='expired_date',
            field=models.DateField(null=True, verbose_name='到期日期'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='figure',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='余额'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='发放金额'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='query_date',
            field=models.DateField(null=True, verbose_name='查询年月'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='years5_overdue',
            field=models.IntegerField(null=True, verbose_name='近五年内逾期月数'),
        ),
        migrations.AddField(
            model_name='summary',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.basic'),
        ),
    ]