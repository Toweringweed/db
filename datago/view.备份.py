from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import contract_t, contract, orders
from datetime import datetime
from django.http import JsonResponse
import json


# def data_trans(df, group_name, cacu_tpye='count', sort_name=''):
#     group_num = ''
#     if cacu_tpye=='count':
#         group_num = df.sort_values(group_name, ascending=True).groupby(group_name).count().reset_index()
#     if cacu_tpye=='sum':
#         group_num = df.sort_values(group_name, ascending=True).groupby(group_name).sum().reset_index()
#     if sort_name != '':
#         group_num = group_num.sort_values(sort_name, ascending=False)
#     group_data = ''
#     ii = ''
#     ii_data = ''
#     ppdata = []
#     for index, i in group_num.iterrows():
#         di = '{name: \'%s\', value: %s }' % (i[0], i[1])
#         group_data += di + ','
#         ii += "\'" + i[0] + "\',"
#         ii_data += str(i[1]) + ','
#         ppdata.append(int(i[1]))
#
#     group_data = '['+group_data[:-1]+']'
#     group_class = '['+ii[:-1]+']'
#     group_pure_data = '['+ii_data[:-1]+']'
#     pdata = str(sorted(ppdata, reverse=True))
#     return {'name_data': group_data, 'name': group_class, 'data': group_pure_data, 'pdata': pdata}
#
# def default(request):
#     f1 = lambda x: numpy.sum(x)
#     f_date = lambda x: datetime.strftime(x, '%Y-%m')
#
#     # 历史全部
#     df1 = pandas.DataFrame(list(contract_t.objects.all().values('money_contract', 'contract_date')))
#     money_contract = "{:,}".format(float('%.2f' % df1[['money_contract']].apply(f1, axis=0)))
#     mm = []
#     ii= ''
#     for i in str(money_contract):
#         if i == ',' or i == '.':
#             ii = '<dd>' + i + '</dd>'
#         else:
#             ii = '<li>' + i + '</li>'
#         mm.append(ii)
#     money_contract = ' '.join(mm)
#
#     order_sum = "{:,}".format(int(len(df1)))
#     df1['month'] = df1['contract_date'].apply(f_date)
#     data_month = data_trans(df1, 'month', 'count')
#
#     # 当前
#     qt2 = contract_t.objects.filter(Q(contract_date__gte=datetime(2017, 8, 11))).\
#         values('city__city', 'customer_name', 'money_contract', 'product_month_id', 'product__product_name')
#     df2 = pandas.DataFrame(list(qt2))
#     df2['product__product_name'] = df2['product__product_name'].apply(lambda x: str(x).replace('A', '').replace('B', '').replace('C', ''))
#     money_contract_today = "{:,}".format(float('%.2f' % df2[['money_contract']].apply(f1, axis=0)))
#
#     data_city = data_trans(df2, 'city__city', 'count', 'customer_name')
#     data_product = data_trans(df2, 'product__product_name', 'count')
#     data_product_month = data_trans(df2, 'product_month_id', 'count')
#
#
#     return render(request, 'default.html', {'data_city': data_city, 'money_contract': money_contract,
#                                           'data_product': data_product, 'order_sum': order_sum,
#                                           'money_contract_today': money_contract_today,
#                                           'data_product_month': data_product_month,
#                                           'data_month': data_month
#                                           }
#                   )

# def test(request):
#     return render(request, 'test.html', {'ll': ll})

def ajax_html(request):
    with open(r'E:\hoomsun_data\db\datago\json\xian.json', 'r', encoding='utf-8') as ff:
        ll = json.load(ff)

    return JsonResponse(ll.name, safe=False)

def ajax_map(request):
    with open(r'E:\hoomsun_data\db\datago\json\city_contract.json', 'r', encoding='utf-8') as ff:
        data = json.load(ff)
    return JsonResponse(data, safe=False)

def ajax_map(request):
    city_j_d = ZhbCdLoanInfo.objects.extra(select={'name': 'store_name'}).values('name', 'store_name').\
        filter(apply_date__regex=today_str).exclude(store_name='').annotate(value=Count('store_name')).order_by('value')
    city_j_m = ZhbCdLoanInfo.objects.extra(select={'name': 'store_name'}).values('store_name', 'name').\
        filter(apply_date__regex=this_month).exclude(store_name='').annotate(value=Count('store_name')).order_by('value')
