from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Avg, Sum, Max, Min, Count, F
from .models import  ZhbCdLoanInfo, ZhbCdLoanbal, ZhbCdLoanCreditInfo, ZhbCdBorrowerInfo, ZhbCdProtoinfo
from datetime import datetime, timedelta
import time
from django.http import JsonResponse
import json

from itertools import chain
from django.views.decorators.cache import cache_page


today_str = '^20170914'
this_month = '^201711'
this_year = '^2017'


@cache_page(60 * 15)
def default(request):
    return render(request, 'default.html')

def ajax_time(request):
    t1 = datetime.now()
    tt = datetime.strftime(t1, '%Y-%m-%d %H:%M:%S')
    return HttpResponse(tt)

# 总合同额计算
def ajax_contract_money(request):
    # old_money = 119057679.93   # 旧数据库中合同金额总和
    old_orders = 1691   # 旧数据库中订单量
    # whole_money = ZhbCdProtoinfo.objects.aggregate(whole_money=Sum('signtotalamt'))
    # whole_money = "{:,}".format(float(whole_money['whole_money']) + old_money)
    whole_money_thisyear = ZhbCdProtoinfo.objects.filter(signdate__regex=this_year).aggregate(whole_money=Sum('signtotalamt'))
    whole_money_thisyear =  "{:,}".format(float(whole_money_thisyear['whole_money']))
    mm = []
    for i in str(whole_money_thisyear):
        if i == ',' or i == '.':
            ii = '<dd>' + i + '</dd>'
        else:
            ii = '<li>' + i + '</li>'
        mm.append(ii)
    money_contract = ' '.join(mm)

    return HttpResponse(money_contract)

# 今日合同额计算
def ajax_contract_today(request):
    today_str = str(datetime.strftime(datetime.today(), '%Y%m%d'))
    person_today_j = ZhbCdLoanInfo.objects.filter(apply_date__regex=today_str).count()
    person_today_s = ZhbCdLoanCreditInfo.objects.filter(Q(final_primary_opinion='01') & Q(apprvfinaltime__regex=today_str)).count()
    person_today_c = ZhbCdProtoinfo.objects.filter(signdate__regex=today_str).count()

    money_today_cc = ZhbCdProtoinfo.objects.filter(signdate__regex=today_str).aggregate(money_today_c=Sum('signtotalamt'))
    try:
        money_today_c = '{:,.1f}'.format(float(money_today_cc['money_today_c']/10000))
    except TypeError:
        money_today_c = 0

    today_jc = {"person_today_j": person_today_j, 'person_today_s': person_today_s,
                'person_today_c': person_today_c, 'money_today_c': money_today_c}
    return JsonResponse(today_jc, safe=False)


city_list = ['安康','宝鸡','保定','滨州','成都','东营','贵阳','汉中','合肥','济南','济宁','昆明','拉萨','兰州',
             '临沂','柳州','南京','南宁','南通','宁波','钦州','青岛','上海','石家庄','苏州','台州','泰安','潍坊',
             '无锡','西安','西安','西宁','咸阳','襄阳','烟台','银川','玉林','镇江','郑州','淄博','遵义'
            ]
department_list = ['安康汉城国际',
            '宝鸡天同国际',
            '保定康泰国际',
            '成都时代八号',
            '东营华泰大厦',
            '贵阳花果园',
            '汉中财富首座',
            '合肥绿地赢海',
            '济南中银大厦',
            '济宁万丽富德',
            '昆明金泰大厦',
            '拉萨哈达滨河花园',
            '兰州金都广场',
            '临沂奥斯卡CBD',
            '柳州桂中大道',
            '南京天时商贸中心',
            '南宁青秀万达',
            '南通金融汇',
            '宁波汇金大厦',
            '钦州阳光曼哈顿',
            '青岛国华大厦',
            '上海南证大厦',
            '石家庄万达广场',
            '苏州新苏大厦',
            '台州天和大厦',
            '泰安万达广场',
            '潍坊万达广场',
            '无锡清扬路',
            '西安锦绣华庭',
            '西安中贸广场',
            '西宁同仁路',
            '咸阳峰汇国际',
            '襄阳盛特区',
            '烟台阳光100',
            '银川紫荆花商务中心',
            '玉林美桥商务中心',
            '镇江中浩国际广场',
            '郑州盛润白宫',
            '淄博潘城国际',
            '遵义航天大厦',
            ]

def ajax_city(request):
    today_str = str(datetime.strftime(datetime.today(), '%Y%m%d'))

    dcc = []
    de_j_d = ZhbCdLoanInfo.objects.filter(apply_date__regex=today_str).values('store_name').annotate(value2=Count('store_name'))
    de_j_m = ZhbCdLoanInfo.objects.filter(apply_date__regex=this_month).values('store_name').annotate(value1=Count('store_name')).order_by('-value1')

    de_j_d = list(de_j_d)
    de_j_m = list(de_j_m)
    j = {'store_name': '', 'value2': 0}
    for i in de_j_m:
        dc = {'name': i['store_name'].replace('营业部', ''), 'value1': i['value1'], 'value2': [j['value2'] for j in de_j_d if j['store_name']==i['store_name']][0] if [j['value2'] for j in de_j_d if j['store_name']==i['store_name']] else 0}
        dcc.append(dc)
    city = {'name_data1': dcc}
    return JsonResponse(city, safe=False)

def ajax_map(request):
    today_str = str(datetime.strftime(datetime.today(), '%Y%m%d'))
    dcc = []
    for i in city_list:
        city_j_d = ZhbCdLoanInfo.objects.filter(Q(apply_date__regex=today_str) & Q(store_name__contains=i)).count()
        # city_j_m = ZhbCdLoanInfo.objects.filter(Q(apply_date__regex=this_month) & Q(store_name__contains=i)).count()

        dc = {'name': i, 'value': city_j_d}
        dcc.append(dc)

    province_j_d = ZhbCdLoanInfo.objects.filter(apply_date__regex=today_str)\
        .extra(select={'prov': 'select rresidence_prov_name from zhb_cd_borrower_info where zhb_cd_borrower_info.LOAN_PK_ID=zhb_cd_loan_info.LOAN_PK_ID'})\
        .values_list('prov')

    # province_j_m = ZhbCdLoanInfo.objects.filter(apply_date__regex=this_month) \
    #     .extra(select={
    #     'prov': 'select rresidence_prov_name from zhb_cd_borrower_info where zhb_cd_borrower_info.LOAN_PK_ID=zhb_cd_loan_info.LOAN_PK_ID'}) \
    #     .values_list('prov')

    province_j_d = list(chain(*list(province_j_d)))
    # province_j_m = list(chain(*list(province_j_m)))
    proo = []
    p_set = list(set(province_j_d))
    for j in p_set:
        ss = {'name': j.replace('省', '').replace('自治区', '').replace('市', '').replace('壮族', '').replace('回族', '').replace('维吾尔', ''),
              'value': province_j_d.count(j)}
        proo.append(ss)

    city_map = {'city': dcc, 'province': proo}

    return JsonResponse(city_map, safe=False)

# 批核率计算
def ajax_hp(request):

    today_str = str(datetime.strftime(datetime.today(), '%Y%m%d'))
    today_30 = datetime.today() - timedelta(days=40)

    hp_month = ZhbCdLoanCreditInfo.objects.filter(apprvfinaltime__regex=this_month).count()
    hp_month_s = ZhbCdLoanCreditInfo.objects.filter(Q(apprvfinaltime__regex=this_month) & Q(final_primary_opinion='01')).count()
    hp_month_ratio = round(hp_month_s/hp_month*100, 1) if hp_month!=0 else 0

    hp_today = ZhbCdLoanCreditInfo.objects.filter(apprvfinaltime__regex=today_str).count()
    hp_today_s = ZhbCdLoanCreditInfo.objects.filter(
        Q(apprvfinaltime__regex=today_str) & Q(final_primary_opinion='01')).count()
    hp_today_ratio = round(hp_today_s/hp_today*100, 1) if hp_today!=0 else 0

    hp_year = ZhbCdLoanCreditInfo.objects.filter(apprvfinaltime__regex=this_year).count()
    hp_year_s = ZhbCdLoanCreditInfo.objects.filter(
        Q(apprvfinaltime__regex=this_year) & Q(final_primary_opinion='01')).count()
    hp_year_ratio = round(hp_year_s / hp_year*100, 1) if hp_year!=0 else 0

    hp = {'hp_month_ratio': hp_month_ratio,  'hp_today_ratio': hp_today_ratio, 'hp_year_ratio': hp_year_ratio}

    # 件均计算
    avg_month = ZhbCdLoanCreditInfo.objects.filter(Q(apprvfinaltime__regex=this_month) & Q(final_primary_opinion='01'))\
        .aggregate(avg_month=Avg('apptcapi'))
    avg_today = ZhbCdLoanCreditInfo.objects.filter(Q(apprvfinaltime__regex=today_str) & Q(final_primary_opinion='01')) \
        .aggregate(avg_today=Avg('apptcapi'))
    avg_year = ZhbCdLoanCreditInfo.objects.filter(Q(apprvfinaltime__regex=this_year) & Q(final_primary_opinion='01')) \
        .aggregate(avg_year=Avg('apptcapi'))
    try:
        avg_today = round(avg_today['avg_today']/10000, 2)
    except TypeError:
        avg_today = 0

    avg = {'avg_month': round(avg_month['avg_month']/10000, 2),
           'avg_today': avg_today,
           'avg_year': round(avg_year['avg_year']/10000, 2)}

    return JsonResponse({'hp':hp, 'avg': avg}, safe=False)

# 近30天进件
def ajax_hp2(request):

    today_30 = datetime.today() - timedelta(days=40)
    today_30_str = str(datetime.strftime(today_30, '%Y%m%d')) + '000000'
    hp2_month = ZhbCdLoanInfo.objects.extra(select={'name': 'round(apply_date/1000000,0)'}). \
        values_list('name').filter(apply_date__gte=today_30_str)

    # 过去30天批核率计算
    hp2_month_shenpi_all = ZhbCdLoanCreditInfo.objects.extra(select={'name': 'round(apprvfinaltime/1000000,0)'}). \
        values_list('name').filter(apprvfinaltime__gte=today_30_str)

    hp2_month_shenpi_get = ZhbCdLoanCreditInfo.objects.extra(select={'name': 'round(apprvfinaltime/1000000,0)'}). \
        filter(final_primary_opinion='01').values_list('name').filter(apprvfinaltime__gte=today_30_str)

    hp2_month = list(chain(*hp2_month))
    hp2_month_a = list(chain(*hp2_month_shenpi_all))
    hp2_month_g = list(chain(*hp2_month_shenpi_get))

    myset = sorted(list(set(hp2_month_a)))

    hp2 = []
    for i in myset:
        dp = {'name': str(i)[4:8], 'value1': hp2_month.count(i),
              'value2': round(hp2_month_g.count(i) / hp2_month_a.count(i) * 100, 1)}
        hp2.append(dp)

    return JsonResponse(hp2, safe=False)

def ajax_hp3(request):
    today = datetime.today()
    today_str2 = str(datetime.strftime(today, '%Y%m%d'))
    today_30 = datetime.today() - timedelta(days=40)
    today_30_str = str(datetime.strftime(today_30, '%Y%m%d')) + '000000'
    hp3_today = ZhbCdLoanCreditInfo.objects.extra(select={'name': 'round(apprvfinaltime/10000,0)'}). \
        filter(apprvfinaltime__regex=today_str2).values_list('name')

    # 近30天审批通过件
    hp3_today_s = ZhbCdLoanCreditInfo.objects.extra(select={'name': 'round(apprvfinaltime/10000,0)'}). \
        filter(Q(final_primary_opinion='01') & Q(apprvfinaltime__regex=today_30_str)).values_list('name')

    # 今日进件
    jj_today = ZhbCdLoanInfo.objects.extra(select={'name': 'round(apply_date/10000,0)'}). \
        filter(apply_date__regex=today_str2).values_list('name')

    hp3_today = list(chain(*hp3_today))
    hp3_today_s = list(chain(*hp3_today_s))
    jj_today = list(chain(*jj_today))

    hp3 = []
    h4 = []
    # 计算今日进件
    for i in range(0, 24):
        if len(str(i)) == 1:
            today_str = round(float(str(today_str2).replace('^', '') + '0' + str(i)), 0)
            dp = {'name': str(i), 'value1': jj_today.count(today_str),
                  'value2': hp3_today.count(today_str)}
        if len(str(i)) == 2:
            today_str = round(float(str(today_str2).replace('^', '') + str(i)), 0)
            dp = {'name': str(i), 'value1': jj_today.count(today_str),
                  'value2': hp3_today.count(today_str)}

        hp3.append(dp)

    return JsonResponse(hp3, safe=False)
