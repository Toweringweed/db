#-*-encoding:utf-8-*-
from _datetime import datetime
# cardid = '6222001001118026958'
# sex = '男' if int(cardid[-2:-1]) % 2 == 1 else '女'
# print(sex)
#
# cd = '20170327060501'
# cd2 = cd[0:4] + '-' + cd[4:6] + '-' + cd[6:8] + ' ' + cd[8:10] + ':' + cd[10:12] + ':' + cd[12:14]
# contract_date = datetime.strptime(cd2, '%Y-%m-%d %H:%M:%S')
#
# print(contract_date)
from personal.mysqldb import ToMysql
import pandas as pd
from dateutil.parser import parse
import numpy as np
import decimal
import re
import string
from datetime import datetime


# read_path = r'E:\hoomsun_data\tt2.csv'
# df = pd.read_csv(read_path, dtype='unicode', encoding='gbk')
#
# for index, row in df.iterrows():
#
#     product_month = int(row['product_month_id'])
#     order_id = str(row['contract_id'])
#     loan_monthly= float(row['repay_month'])
#     contract_money = float(row['residual_money2'])
#     r1= float(row['residual_money'])
#     period = int(row['period'])
#     rate = np.rate(product_month, -loan_monthly, contract_money, fv=0)
#     r2 = 0
#     print(period)
#     for i in range(1, period):
#         residual_money = -np.ppmt(rate, i, product_month, contract_money)
#         r2 = r2 + residual_money
#         print(i)
#
#     print(r1, r2)

# order_id = 'XALD20150731002'
# order_time = re.findall(re.compile(r'\D(20\d{6})'), order_id)
# order_time2 = parse(order_time[0]) if order_time else None
# print(order_time2)
#
# print(np.mean([5,6,8]))

# df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
#  'key2':['one', 'two', 'one', 'two', 'one'],
#  'data1': np.random.randn(5),
#  'data2': np.random.randn(5)},)
#
# gg = df.groupby('key1').count()
# gt =dict(gg['key2'])
#
# data = []
# for i in gt:
#     dd = {'name': i, 'value': gt[i]}
#     data.append(dd)

# dd = {}
# print(gt.keys())
# print(gt.index())
# print(gt['key2'])
#
# a="{:,}".format(12345678.23)
# print(a)
#
# import pymysql
# kwargs = {'host': '',
#           'user': 'root',
#           'passwd': 'Myluoxue99..',
#           'db': 'hoomsun',
#           'charset': 'utf8'}
# #
# conn = pymysql.connect(host='localhost',user ='root', passwd ='Myluoxue99..', db = 'hoomsun', charset ='utf8')
# sql = "select * from datago_contract_t"
# df = pd.read_sql(sql, conn)
# f1 = lambda x: str(x).replace('C', '')
# f_date = lambda x: datetime.strftime(x, '%Y-%m')
# df['month'] = df['contract_date'].apply(f_date)
# group_num = df[['month', 'contract_date']].sort_values('month', ascending=True).groupby('month').count().reset_index()
# print(group_num)
#
#
# # path = r'C:\Python34\NEWS.txt'
# # df = pd.read_csv(path, sep=',')
# # print(df)
#
# a = [3, 4, 5, 1]
# ll = []
# for i in a:
#     ll.append(i)
#
# b = sorted(ll,reverse=True)
# print(b)
import json
#
# with open(r'E:\hoomsun_data\db\datago\json\xian.json', 'r', encoding='utf-8') as ff:
#     ll = json.load(ff)
#     st = str(ll).replace('"', '')
# print(ll)

#
# department_list = ['安康汉城国际营业部',
#                    '宝鸡天同国际营业部',
#                    '保定康泰国际营业部',
#                    '滨州国际大厦营业部',
#                    '成都时代八号营业部',
#                    '东营华泰大厦营业部',
#                    '贵阳花果园营业部',
#                    '汉中财富首座营业部',
#                    '合肥绿地赢海营业部',
#                    '济南中银大厦营业部',
#                    '济宁万丽富德营业部',
#                    '昆明金泰大厦营业部',
#                    '拉萨哈达滨河花园营业部',
#                    '兰州金都广场营业部',
#                    '临沂奥斯卡CBD营业部',
#                    '柳州桂中大道营业部',
#                    '南京天时商贸中心营业部',
#                    '南宁青秀万达营业部',
#                    '南通金融汇营业部',
#                    '宁波汇金大厦营业部',
#                    '钦州阳光曼哈顿营业部',
#                    '青岛国华大厦营业部',
#                    '上海南证大厦营业部',
#                    '石家庄万达广场营业部',
#                    '苏州新苏大厦营业部',
#                    '台州天和大厦营业部',
#                    '泰安万达广场营业部',
#                    '潍坊万达广场营业部',
#                    '无锡清扬路营业部',
#                    '西安锦绣华庭营业部',
#                    '西安中贸广场营业部',
#                    '西宁同仁路营业部',
#                    '咸阳峰汇国际营业部',
#                    '襄阳盛特区营业部',
#                    '烟台阳光100营业部',
#                    '银川紫荆花商务中心营业部',
#                    '玉林美桥商务中心营业部',
#                    '镇江中浩国际广场营业部',
#                    '郑州盛润白宫营业部',
#                    '淄博潘城国际营业部',
#                    '遵义航天大厦营业部',
#                    ]
#
# city_j_d = [{'store_name': '保定康泰国际营业部', 'value': 30}, {'store_name':'遵义航天大厦营业部', 'value':40}]
# dict_city = []
# j = ''
# for i in department_list:
#     for j in city_j_d:
#         if i == j['store_name']:
#             dc = {'name': i, 'value1': j['value'],
#                   }
#             dict_city.append(dc)
# city = {'name': dict_city}
# print(city)

import time
# today =
#
# print(rr)

# name = input('please enter your name: ')
# print(name)

today_str = '^20170904'
h4 = []
for i in range(0, 9):
    today_str = float(str(today_str).replace('^', '') + '0' + str(i))
    h4.append(today_str)
print(h4)