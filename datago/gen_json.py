from personal.mysqldb import ToMysql
import pymysql
import pandas as pd
from dateutil.parser import parse
import numpy as np
import json
import decimal
import re
import string
from datetime import datetime
import time

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

def data_trans(df, group_name, cacu_tpye='count', sort_name=''):
    group_num = ''
    if cacu_tpye=='count':
        group_num = df.sort_values(group_name, ascending=True).groupby(group_name).count().reset_index()
    if cacu_tpye=='sum':
        group_num = df.sort_values(group_name, ascending=True).groupby(group_name).sum().reset_index()
    if sort_name != '':
        group_num = group_num.sort_values(sort_name, ascending=False)
    group_data = ''
    ii = ''
    ii_data = ''
    data = []
    name = []
    name_data = []
    for index, i in group_num.iterrows():
        di = '{name: \'%s\', value: %s }' % (i[0], i[1])
        group_data += di + ','
        ii += "\'" + i[0] + "\',"
        ii_data += str(i[1]) + ','
        name_data_dict = {'name': i[0], 'value': int(i[1])}
        data.append(int(i[1]))
        name.append(i[0])
        name_data.append(name_data_dict)

    group_data_str = '['+group_data[:-1]+']'
    group_class = '['+ii[:-1]+']'
    group_pure_data = '['+ii_data[:-1]+']'

    return {'name_data': group_data_str, 'name': name, 'data': data, 'name_data2': name_data, 'name_data1': name_data}

conn = pymysql.connect(host='localhost',user ='root', passwd ='Myluoxue99..', db = 'hoomsun', charset ='utf8')
sql = "select * from datago_contract_t"
df = pd.read_sql(sql, conn)
f1 = lambda x: np.sum(x)
money_contract = "{:,}".format(float('%.2f' % df[['money_contract']].apply(f1, axis=0)))
mm = []
ii= ''
for i in str(money_contract):
    if i == ',' or i == '.':
        ii = '<dd>' + i + '</dd>'
    else:
        ii = '<li>' + i + '</li>'
    mm.append(ii)
money_contract = ' '.join(mm)
f_json = money_contract

with open("json/xian.json","w") as dump_f:
    json.dump(f_json, dump_f)

sql2 = r"select datago_contract_t.*, datago_product.product_name, datago_city.city from datago_contract_t left join " \
       "datago_product on datago_contract_t.product_id = datago_product.product_id left join datago_city on " \
       "datago_contract_t.city_id = datago_city.city_id where datago_contract_t.contract_date >= '2017-08-01'"


sql_today = r"select datago_contract_t.*, datago_product.product_name, datago_city.city from datago_contract_t left join " \
       "datago_product on datago_contract_t.product_id = datago_product.product_id left join datago_city on " \
       "datago_contract_t.city_id = datago_city.city_id where datago_contract_t.contract_date = '2017-08-11'"

# sql3 = "select * from datago_contract_t where contract_date like '2017-08-11%'"

df2 = pd.read_sql(sql2, conn)
df2['product_name'] = df2['product_name'].apply(lambda x: str(x).replace('A', '').replace('B', '').replace('C', ''))
money_contract_month = "{:,}".format(float('%.2f' % df2[['money_contract']].apply(f1, axis=0)))

data_city = data_trans(df2, 'city', 'count', 'customer_name')
# data_product = data_trans(df2, 'product__product_name', 'count')
# data_product_month = data_trans(df2, 'product_month_id', 'count')

city_json = data_city

with open("json/city_contract.json", "w", encoding='utf-8') as dump_f:
    json.dump(city_json, dump_f, ensure_ascii=False)

v_img = open(r'json/city_contract.txt', 'w')
v_img.write(str(city_json))
v_img.close()




df3 = pd.read_sql(sql_today, conn)
df3['product_name'] = df3['product_name'].apply(lambda x: str(x).replace('A', '').replace('B', '').replace('C', ''))
count_contract_today = df3[['money_contract']].apply(lambda x: x.count(), axis=0).tolist()
money_contract_today = df3[['money_contract']].apply(f1, axis=0).tolist()

contract_today = {'count': count_contract_today, 'money': money_contract_today}

with open("json/contract_today.json", "w", encoding='utf-8') as dump_f:
    json.dump(contract_today, dump_f, ensure_ascii=False)





