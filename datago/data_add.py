from personal.mysqldb import ToMysql
import pandas as pd
from dateutil.parser import parse
import numpy as np
import decimal
import re
import string
from datetime import datetime
import time


kwargs = {'host': 'localhost',
          'user': 'root',
          'passwd': 'Myluoxue99..',
          'db': 'hoomsun',
          'charset': 'utf8'}
sql = ToMysql(kwargs)

# 合并数据
# read_path1 = r'E:\hoomsun_data\数据岗所需数据1.xls'
# df1 = pd.read_excel(read_path1)
# df1['身份证号'] = df1['身份证号'].astype(str)
#
# read_path2 = r'E:\hoomsun_data\数据岗所需数据2.xls'
# df2 = pd.read_excel(read_path2)
# df2['身份证号'] = df2['身份证号'].astype(str)
#
# df = pd.concat([df1, df2], axis=0, join_axes=None, ignore_index=True)
#
# df = df.drop_duplicates(subset=['申请流水号', '身份证号'], keep='first')
#
# save_path = r'E:\hoomsun_data\userdata_m8.csv'
# pd.DataFrame.to_csv(df, save_path, sep=',', index=None)


# read_path = r'E:\hoomsun_data\userdata_m8.csv'
# df = pd.read_csv(read_path, encoding='gbk', dtype='unicode')

# 产品表
# product = [
#     ['aj', '安居贷'],
#     ['ajA', '安居贷A'],
#     ['ajB', '安居贷B'],
#     ['ajC', '安居贷C'],
#
#     ['hs', '红商贷'],
#     ['hsA', '红商贷A'],
#     ['hsB', '红商贷B'],
#     ['hsC', '红商贷C'],
#
#     ['kx', '开薪贷'],
#     ['kxA', '开薪贷A'],
#     ['kxB', '开薪贷B'],
#     ['kxC', '开薪贷C'],
#
#     ['ry', '融易贷'],
#     ['ryA', '融易贷A'],
#     ['ryB', '融易贷B'],
#     ['ryC', '融易贷C'],
#
#     ['xj', '薪居贷'],
#     ['xjA', '薪居贷A'],
#     ['xjB', '薪居贷B'],
#     ['xjC', '薪居贷C'],
# ]
# for p in product:
#     p_dict = {
#         'product_id': p[0],
#         'product_name': p[1],
#         'update_time': time.localtime()
#     }
#     sql.into('datago_product', **p_dict)

# product_month = [
#     ['12', 12],
#     ['18', 18],
#     ['24', 24],
#     ['36', 36],
#     ['48', 48]
#
# ]
# for p in product_month:
#     p_dict = {
#         'product_month_id': p[0],
#         'product_month': p[1],
#         'update_time': time.localtime()
#     }
#     sql.into('datago_product_month', **p_dict)


# read_path2 = r'E:\hoomsun_data\userdata_m8.csv'
# df2 = pd.read_csv(read_path2, encoding='gbk', dtype='unicode')
#
# df2 = df2[df2['身份证号'].str.len()>10]
# df2 = df2[100:]
#
# fillna_list = ['核实收入金额(初审)', '核实负债金额(初审)', '理论审批金额(初审)', '信用负债率(初审)']
#
# for fi in fillna_list:
#     df2[fi] = df2[fi].fillna(-99)
#
# for index, row in df2.iterrows():
#     print(index)
#     idcard = str(row['身份证号']).strip()
#
#     sex = '男' if int(idcard[-2:-1]) % 2 == 1 else '女'
#     com_dict = {
#         'customer_id': idcard,
#         'customer_name': str(row['客户姓名']).strip(),
#         'Idcard': idcard,
#         'sex': sex,
#         'update_time': time.localtime()
#     }
#     sql.into('datago_customer', **com_dict)
#
#     order_id = str(row['申请流水号']).strip()
#     product = str(row['申请产品']).strip() if str(row['申请产品']) != 'nan' else ''
#     order_time = re.findall(re.compile(r'\D(20\d{6})'), order_id)
#     order_time2 = parse(order_time[0]) if order_time else None
#
#     p1 = product.split('-')
#     p11 = p1[0].replace('安居贷', 'aj').replace('融易贷', 'ry').replace('薪居贷', 'xj').replace('红商贷', 'hs').replace('开薪贷', 'kx')
#     apply_money = str(row['申请金额']).strip()
#     re1 = re.findall(r'\d+', apply_money)
#     a_m = int(re1[0]) if re1 else None
#
#     orders_dict = {
#         'order_id': order_id,
#         'product_id': p11,
#         'product_month_id': p1[1],
#         'customer_id': idcard,
#         'marketing_channel': str(row['销售渠道']).strip() if str(row['销售渠道']) != 'nan' else '',
#         'customer_source': str(row['客户来源']).strip() if str(row['客户来源']) != 'nan' else '',
#         'type': '线下',
#         'order_date': order_time2,
#         'money_apply': a_m,
#         'urgent': str(row['紧急程度']).strip() if str(row['紧急程度']) != 'nan' else '',
#         'enterprise_credit': str(row['是否有工商网信息']).strip() if str(row['是否有工商网信息']) != 'nan' else '',
#         'enterprise_credit_bz': str(row['备注1']),
#         'court': str(row['法院网核查']),
#         'address_proven': str(row['是否有住址证明']).strip(),
#         'private_owner': True if str(row['是否私营业主']).strip()=="是" else False,
#         'address_proven_bz': str(row['备注2']),
#         'continues': True if str(row['是否续借']).strip()=='是' else False,
#         'verify_income_initial': '%.2f' % decimal.Decimal(row['核实收入金额(初审)']) if row['核实收入金额(初审)']!=-99 else None,
#         'verify_indebted_initial': "%.2f" % decimal.Decimal(row['核实负债金额(初审)']) if row['核实负债金额(初审)'] !=-99 else None,
#         'verify_money_initial': "%.2f" % decimal.Decimal(row['理论审批金额(初审)']) if row['理论审批金额(初审)'] != -99 else None,
#         'debt_ratio_initial': "%.2f" % decimal.Decimal(row['信用负债率(初审)']) if row['信用负债率(初审)'] !=-99 else None,
#         'opinion_initial': str(row['初审内部意见']),
#         'material_evaluation': str(row['贷款资料评估']),
#         'credit_evaluation': str(row['信用信息评估']),
#         'risk': str(row['信用风险点']),
#         'update_time': time.localtime()
#     }
#     sql.into('datago_orders', **orders_dict)
#
#     hukou_dic = {
#         'customer_id': idcard,
#         'order_id': order_id,
#         'home_province': str(row['户口所在省']).strip() if str(row['户口所在省']) != 'nan' else '',
#         'home_city': str(row['户口所在市']).strip() if str(row['户口所在市']) != 'nan' else '',
#         'home_district': str(row['户口所在区']).strip() if str(row['户口所在区']) != 'nan' else '',
#         'update_time': time.localtime()
#     }
#     sql.into('datago_hukou', **hukou_dic)
#
#     edu_dic = {
#         'customer_id': idcard,
#         'order_id': order_id,
#         'education': str(row['学历']).strip(),
#         'college': '',
#         'update_time': time.localtime()
#
#     }
#     sql.into('datago_education', **edu_dic)
#
#     reside_time = re.findall(re.compile(r'\d{6}'), str(row['起始居住地时间']).strip())
#     rt1 = datetime.strptime(reside_time[0][0:4] + '-' + reside_time[0][4:6] + '-' + '01', '%Y-%m-%d') if reside_time else None
#     rent = re.findall(re.compile(r'\d+'), str(row['租金月还']).strip())
#     rent2 = int(rent[0]) if rent else None
#     bt_time = re.findall(re.compile(r'\d{6}'), str(row['来本地年份']).strip())
#     bt1 = datetime.strptime(bt_time[0][0:4] + '-' + bt_time[0][4:6] + '-' + '01', '%Y-%m-%d') if bt_time else None
#
#     reside_dic = {
#         'customer_id': idcard,
#         'order_id': order_id,
#         'reside_time': rt1,
#         'reside_conditions': str(row['居住状况']).strip() if str(row['居住状况']) != 'nan' else '',
#         'rent': rent2,
#         'reside_province': str(row['住宅所在省']).strip() if str(row['住宅所在省']) != 'nan' else '',
#         'reside_city': str(row['住宅所在市']).strip() if str(row['住宅所在市']) != 'nan' else '',
#         'reside_district': str(row['住宅所在区']).strip() if str(row['住宅所在区']) != 'nan' else '',
#         'arrival_time': bt1,
#         'update_time': time.localtime()
#     }
#     sql.into('datago_reside', **reside_dic)
#
#     st_time = re.findall(re.compile(r'\d{6}'), str(row['起始服务时间']).strip())
#     st1 = datetime.strptime(st_time[0][0:4] + '-' + st_time[0][4:6] + '-' + '01', '%Y-%m-%d') if st_time else None
#
#     occu_dic = {
#         'customer_id': idcard,
#         'order_id': order_id,
#         'company': '',
#         'service_time': st1,
#         'positions': '',
#         'levels ': str(row['职位级别']).strip() if str(row['职位级别']) != 'nan' else '',
#         'department': '',
#         'industry': str(row['所属行业']).strip() if str(row['所属行业']) != 'nan' else '',
#         'category': str(row['单位性质']).strip() if str(row['单位性质']) != 'nan' else '',
#         'pay': '',
#         'scope': '',
#         'social_security': '',
#         'company_province': str(row['单位地址(省)']).strip() if str(row['单位地址(省)']) != 'nan' else '',
#         'company_city': str(row['单位地址(市)']).strip() if str(row['单位地址(市)']) != 'nan' else '',
#         'company_district': str(row['单位地址(区)']).strip() if str(row['单位地址(区)']) != 'nan' else '',
#         'update_time': time.localtime()
#     }
#     sql.into('datago_occupation', **occu_dic)
#     house_dict ={
#         'customer_id': idcard,
#         'order_id': order_id,
#         'marital_status': str(row['婚姻情况']).strip() if str(row['婚姻情况']) != 'nan' else '',
#         'update_time': time.localtime()
#     }
#     sql.into('datago_household', **house_dict)
#
#     in1 = decimal.Decimal(row['银行流水第一个月(合计)'])
#     in2 = decimal.Decimal(row['银行流水第二个月(合计)'])
#     in3 = decimal.Decimal(row['银行流水第三个月(合计)'])
#     in4 = decimal.Decimal(row['银行流水第四个月(合计)'])
#     in5 = decimal.Decimal(row['银行流水第五个月(合计)'])
#     in6 = decimal.Decimal(row['银行流水第六个月(合计)'])
#
#     a = [in1, in2, in3, in4, in5, in6]
#     in_mean = np.mean(a) if np.mean(a) == np.mean(a) else None
#
#     in_std = np.std(a) if np.std(a) == np.std(a) else None
#     in_var = in_std/in_mean if in_std is not None and in_mean != 0  else None
#
#     in1 = '%.3f' % in1 if in1 == in1 else None
#     in2 = '%.3f' % in2 if in2 == in2 else None
#     in3 = '%.3f' % in3 if in3 == in3 else None
#     in4 = '%.3f' % in4 if in4 == in4 else None
#     in5 = '%.3f' % in5 if in5 == in5 else None
#     in6 = '%.3f' % in6 if in6 == in6 else None
#
#     income_dict = {
#         'customer_id': idcard,
#         'order_id': order_id,
#         'bank_in1': in1,
#         'bank_in2': in2,
#         'bank_in3': in3,
#         'bank_in4': in4,
#         'bank_in5': in5,
#         'bank_in6': in6,
#         'income_type': '个人',
#         'income_habit': '',
#         'bank_mean':  '%.3f' % in_mean if in_mean else None,
#         'bank_std': '%.3f' % in_std if in_std else None,
#         'bank_var': '%.3f' % in_var if in_var else None,
#         'update_time': time.localtime()
#     }
#     sql.into('datago_income', **income_dict)

    #
    # product_add = {
    #     'product_id': '99',
    #
    # }

# read_path = r'E:\hoomsun_data\综合放款台账-8.24.xlsx'
# df = pd.read_excel(io=read_path)
#
# for index, row in df.iterrows():
#     idcard = str(row['身份证号码']).strip()
#     order_id = str(row['合同编号']).strip()
#     # sex = '男' if int(idcard[-2:-1]) % 2 == 1 else '女'
#     # com_dict = {
#     #     'customer_id': idcard,
#     #     'customer_name': str(row['客户姓名']).strip(),
#     #     'Idcard': idcard,
#     #     'sex': sex,
#     #     'update_time': time.localtime()
#     # }
#     # sql.into('datago_customer', **com_dict)
#     city = str(row['城市']).strip() if str(row['城市']) != 'nan' else ''
#     city_id = sql.select("select city_id from datago_city where city='%s'" % city) if city != '' else 'unknown'
#     department = str(row['营业部']).strip() if str(row['营业部']) != 'nan' else ''
#     region = str(row['区域']).strip() if str(row['区域']) != 'nan' else ''
#     department_id = sql.select("select department_id from datago_department where department='%s'" % department) if department != '' else 'unknown'
#     region_id = sql.select("select region_id from datago_region where region='%s'" % region)
#     product = str(row['核批产品']).strip()
#     product_id = sql.select("select product_id from datago_product where product_name='%s'" % product)
#
#     cont = {
#         'contract_id ': order_id,
#         'idcard': idcard,
#         'customer_id': idcard,
#         'customer_name': str(row['客户姓名']).strip() if str(row['客户姓名']) != 'nan' else '',
#         'bank_account': str(row['银行卡号']).strip() if str(row['银行卡号']) != 'nan' else '',
#         'city_id': city_id,
#         'region_id': region_id,
#         'department_id': department_id,
#         'date_shencha': datetime.strptime(str(row['放款审查日期']), '%Y-%m-%d %H:%M:%S') if str(row['放款审查日期']) != 'NaT' else None,
#         'date_fangkuan': datetime.strptime(str(row['放款日期']), '%Y-%m-%d %H:%M:%S') if str(row['放款日期']) != 'NaT' else None,
#         'contract_date': datetime.strptime(str(row['合同签约日期']), '%Y-%m-%d %H:%M:%S') if str(row['合同签约日期']) !='NaT' else None,
#         'result_shencha': str(row['放款审查结果']).strip() if str(row['放款审查结果']) != 'nan' else '',
#         'product_id': product_id,
#         'product_month_id': str(row['核批期限']),
#         'money_pihe': int(row['核批金额']) if str(row['核批金额']) != 'nan' else None,
#         'money_contract': '%.2f' % decimal.Decimal(row['合同金额']) if str(row['合同金额']) !='nan' else None,
#         'money_month': '%2f' % decimal.Decimal(row['月还款额']) if str(row['月还款额']) != 'nan' else None,
#         'qianyuetiaojian': str(row['签约条件']),
#         'fangkuanbeizhu': str(row['备注']),
#         'tuihuiyuanyin': str(row['退回原因']),
#         'update_time': time.localtime()
#     }
#     sql.into('datago_contract_t', index, id=order_id, **cont)

# read_path = r'E:\hoomsun_data\客户放款情况表.xlsx'
# df = pd.read_excel(read_path)
# #
# for index, row in df.iterrows():
#     cardid = str(row[2])
#     order_id = str(row[0])
#     sex = '男' if int(cardid[-2:-1])%2 == 1 else '女'
#     com_dict = {
#         'customer_id': str(row[2]),
#         'customer_name': str(row[1]),
#         'Idcard': cardid,
#         'sex': sex
#     }
#     sql.into('datago_customer', **com_dict)
#     cd = str(row[6])
#     cd2 = cd[0:4] + '-' + cd[4:6] + '-' + cd[6:8] + ' ' + cd[8:10] + ':' + cd[10:12] + ':' + cd[12:14]
#     contract_date = datetime.strptime(cd2, '%Y-%m-%d %H:%M:%S')
#
#     fq = str(row[7])
#     fq2 = fq[0:4] + '-' + fq[4:6] + '-' + fq[6:8] + ' ' + fq[8:10] + ':' + fq[10:12] + ':' + fq[12:14]
#     loan_date = datetime.strptime(fq2, '%Y-%m-%d %H:%M:%S')
#
#     rd_s = str(row[9])
#     rd_s2 = rd_s[0:4] + '-' + rd_s[4:6] + '-' + rd_s[6:8]
#     repay_date_start = datetime.strptime(rd_s2, '%Y-%m-%d')
#
#     rd_e = str(row[10])
#     rd_e2 = rd_e[0:4] + '-' + rd_e[4:6] + '-' + rd_e[6:8]
#     repay_date_end = datetime.strptime(rd_e2, '%Y-%m-%d')
#
#     product = str(row[3])
#     p1 = product.split('-')
#     p11 = p1[0].replace('安居贷', 'aj').replace('融易贷', 'ry').replace('薪居贷', 'xj').replace('红商贷', 'hs').replace('开薪贷', 'kx')
#
#     month = int(p1[1])
#
#     loan_monthly = float(row[5])
#     contract_money = float(row[4])
#
#     rate = -np.rate(month, -loan_monthly, contract_money, fv=0)
#     loan_rate = '%.3f' %(rate)
#
#     contract_dic = {
#         'contract_id': order_id,
#         'customer_id': cardid,
#         'order_id': order_id,
#         'contract_date': contract_date,
#         'loan_date': loan_date,
#         'repay_date_start': repay_date_start,
#         'repay_date_end': repay_date_end,
#         'contract_money': contract_money,
#         'approved_money': decimal.Decimal(float(row[5])),
#         'loan_monthly': decimal.Decimal(loan_monthly),
#         'product_id': p11,
#         'rate': loan_rate,
#         'online': '线下',
#         'pos': '',
#         'update_time': time.localtime()
#     }
#     sql.into('datago_contract', index, id=order_id, **contract_dic)
#
#
# # read_path = r'E:\hoomsun_data\test.xlsx'
# # df = pd.read_excel(read_path)
# #
# #
# for index, row in df.iterrows():
#     if index>=1:
#         if (df.at[index, '合同编号'] == df.at[index-1, '合同编号']) & (row['期初剩余本金'] != row['期初剩余本金']):
#             df.at[index, '期初剩余本金'] = df.at[index-1, '期初剩余本金']
#         if (df.at[index, '合同编号'] == df.at[index-1, '合同编号']) & (row['计算期初剩余本金'] != row['计算期初剩余本金']):
#             df.at[index, '计算期初剩余本金'] = df.at[index-1, '计算期初剩余本金']
# #


# read_path = r'E:\hoomsun_data\规整数据8.24.xlsx'
# df = pd.read_excel(read_path)
#
# for index, row in df.iterrows():
#     print(index)
#     if index>=1:
#         if (df.at[index, '合同编号'] == df.at[index-1, '合同编号']) & (row['期初剩余本金'] != row['期初剩余本金']):
#             df.at[index, '期初剩余本金'] = df.at[index-1, '期初剩余本金']
#         if (df.at[index, '合同编号'] == df.at[index-1, '合同编号']) & (row['计算期初剩余本金'] != row['计算期初剩余本金']):
#             df.at[index, '计算期初剩余本金'] = df.at[index-1, '计算期初剩余本金']
#
# save_path = r'E:\hoomsun_data\规整数据8.28.csv'
# pd.DataFrame.to_csv(df, save_path, sep=',', index=None)

# read_path = r'E:\hoomsun_data\规整数据8.28.csv'
# df = pd.read_csv(read_path, dtype='unicode', encoding='gbk')
#
# df = df[df['还款日期'] == df['报表日期']]
#
# save_path = r'E:\hoomsun_data\规整数据-去重8.28.csv'
# pd.DataFrame.to_csv(df, save_path, sep=',', index=None)

# read_path = r'E:\hoomsun_data\规整数据-去重8.28.csv'
# df = pd.read_csv(read_path, dtype='unicode', encoding='gbk')
#
# for index, row in df.iterrows():
#     print(index)
#     order_id = str(row['合同编号'])
#     product = re.findall(re.compile(r'\d{2}'), str(row['产品类型']))
#     product_month = str(product[0]) if product else ''
#
#     repay_dict = {
#         'repayment_id': order_id + str(row['报表日期']),
#         'contract_id': order_id,
#         'customer_name': str(row['客户名称']).strip(),
#         'bank_account': '',
#         'residual_money': '%.2f' % decimal.Decimal(row['期初剩余本金']),
#         'residual_money2': '%.2f' % decimal.Decimal(row['计算期初剩余本金']),
#         'period': int(row['当期期次']),
#         'product_month_id': product_month,
#         'repay_date': datetime.strptime(str(row['报表日期']), '%Y-%m-%d') if str(row['报表日期']) != 'NaT' else None,
#         'should_date': datetime.strptime(str(row['还款日期']), '%Y-%m-%d') if str(row['还款日期']) != 'NaT' else None,
#         'actual_date': None,
#         'repay_condition': str(row['备注']) if str(row['备注']) != 'nan' else '',
#         'repay_overdue': 0 if (str(row['备注']).strip() == '扣款成功') | (str(row['备注']).strip() == '存公成功') |
#                               (str(row['备注']).strip() == '交易成功') | (str(row['备注']).strip() == '提前还款') else 1,
#         'yuqi_qici': int(str(row['逾期期数']).strip()) if str(row['逾期期数']).strip() != 'nan' else 0,
#         'update_time': time.localtime()
#
#     }
#     sql.into('datago_repayment', **repay_dict)

read_path = r'E:\hoomsun_data\规整数据-去重8.28.csv'
df = pd.read_csv(read_path, dtype='unicode', encoding='gbk')

for index, row in df.iterrows():
    print(index)
    order_id = str(row['合同编号'])
    repayment_id = order_id + str(row['报表日期'])
    repay_month = float(row['月还款额'])

    sql_t = "update datago_repayment set repay_month=%.2f where repayment_id='%s'" % (repay_month, repayment_id)

    print(sql_t)

    sql.updates(sql_t)



# read_path = r'E:\hoomsun_data\综合台账.xlsx'
# df = pd.read_csv(read_path, dtype='unicode', encoding='gbk')
#
# for index, row in df.iterrows():
#     print(index)
#     cardid = str(row['身份证号码']).strip()
#     product = re.findall(re.compile(r'\d{2}'), str(row['产品类型']))
#     product_month = str(product[0]) if product else ''
#
#     repay_dict = {
#         'customer_name': str(row['申请人']).strip(),
#         'idcard': cardid,
#         'bank_account': '',
#         'residual_money': '%.2f' % decimal.Decimal(row['期初剩余本金']),
#         'residual_money2': '%.2f' % decimal.Decimal(row['计算期初剩余本金']),
#         'period': int(row['当期期次']),
#         'product_month_id': product_month,
#         'repay_date': datetime.strptime(str(row['报表日期']), '%Y-%m-%d') if str(row['报表日期']) != 'NaT' else None,
#         'should_date': datetime.strptime(str(row['还款日期']), '%Y-%m-%d') if str(row['还款日期']) != 'NaT' else None,
#         'actual_date': None,
#         'repay_condition': str(row['备注']) if str(row['备注']) != 'nan' else '',
#         'repay_overdue': 0 if (str(row['备注']).strip() == '扣款成功') | (str(row['备注']).strip() == '存公成功') |
#                               (str(row['备注']).strip() == '交易成功') | (str(row['备注']).strip() == '提前还款') else 1,
#         'yuqi_qici': int(str(row['逾期期数']).strip()) if str(row['逾期期数']).strip() != 'nan' else 0,
#         'update_time': time.localtime()
#
#     }
#     sql.into('datago_repayment', **repay_dict)



