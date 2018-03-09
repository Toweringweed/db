import pymysql
from sqlalchemy import create_engine
import json
from datetime import datetime


conn = pymysql.connect(host='192.168.1.178', user='root', passwd='root', port=3307, db='xindai20180206', charset='utf8')

# 连接新信销系统
engine = create_engine("oracle://credit_reader:reader2018@113.200.105.35:1521/ORCL")

# sql_card = r'SELECT CREDIT_BASIC.ID_CARD,CREDIT_BASIC.REPORTTIME,CREDIT_CARD.BANK,CREDIT_CARD.ACCOUNT_TYPE,CREDIT_CARD.GRANT_DATE,CREDIT_CARD.ACCOUNT_STATE,CREDIT_CARD.QUERY_DATE,CREDIT_CARD.CREDIT_LINE,CREDIT_CARD.USED_LINE,CREDIT_CARD.OVERDUE,CREDIT_CARD.FIVE_YEARS_OVERDUE,CREDIT_CARD.NINETY_DAYS_OVERDUE,CREDIT_CARD.OVERDUE_MONEY FROM CREDIT_CARD LEFT JOIN CREDIT_BASIC ON CREDIT_BASIC.UUID = CREDIT_CARD.UUID'
# sql_loan = r'SELECT CREDIT_BASIC.ID_CARD,CREDIT_BASIC.REPORTTIME,CREDIT_LOAN.INSTITUTION,CREDIT_LOAN.GRANT_DATE,CREDIT_LOAN.MONEY,CREDIT_LOAN.EXPIRED_DATE,CREDIT_LOAN.QUERY_DATE,CREDIT_LOAN.FIGURE,CREDIT_LOAN.OVERDUE,CREDIT_LOAN.YEARS5_OVERDUE,CREDIT_LOAN.DAYS90_OVERDUE,CREDIT_LOAN.YUQI_MONEY,CREDIT_LOAN.TYPE,CREDIT_LOAN.LOAN_STATE,CREDIT_LOAN.ACCOUNT_CATEGORY_MAIN FROM CREDIT_BASIC LEFT JOIN CREDIT_LOAN ON CREDIT_BASIC.UUID = CREDIT_LOAN.UUID'

# sql_basic = r"select sum(CON_AMOUNT) from CREDIT_BASIC"
# ss = engine.execute(sql_basic).fetchall()

def get_sum(cur, target_column, table_name, conditional_column, get_date):
    sql = r"select sum(%s) from %s where %s like '%s'" % (target_column, table_name, conditional_column, get_date)
    cur.execute(sql)
    return cur.fetchall()

def get_sum_new(cur, target_column, table_name, conditional_express):
    sql = r"select sum(%s) from %s where %s" % (target_column, table_name, conditional_express)
    return cur.execute(sql).fetchall()

mn201801 = get_sum_new(cur=engine, target_column='CON_AMOUNT', table_name='HS_CONTRACT', conditional_express="SIGN_TIME > TO_DATE('2018-01-01 00:00:00', 'yyyy-mm-dd hh24:mi:ss')")

# # 计算历年合同金额  方式一： 放款合同额； 方式二：签约合同额
# m2015 = get_sum(cur=conn.cursor(),  target_column='SIGNTOTALAMT', table_name='zkbc_cd_loanbal', conditional_column='BEGINDATE', get_date='2015%')
# print(m2015)
# m2016 = get_sum(cur=conn.cursor(),  target_column='SIGNTOTALAMT', table_name='zkbc_cd_loanbal', conditional_column='BEGINDATE', get_date='2016%')
# print(m2016)
# m2017 = get_sum(cur=conn.cursor(),  target_column='SIGNTOTALAMT', table_name='zkbc_cd_loanbal', conditional_column='BEGINDATE', get_date='2017%')
# print(m2017)
#
# ms2017 = get_sum(cur=conn.cursor(),  target_column='SIGNTOTALAMT', table_name='zkbc_cd_protoinfo', conditional_column='signdate', get_date='2017%')
# print(ms2017)

# m201801 = get_sum(cur=conn.cursor(),  target_column='SIGNTOTALAMT', table_name='zkbc_cd_loanbal', conditional_column='BEGINDATE', get_date='201801%')



mn_today = get_sum_new(cur=engine, target_column='CON_AMOUNT', table_name='HS_CONTRACT', conditional_express="TRUNC(SIGN_TIME) = TRUNC(SYSDATE)")
print(mn_today)

m2015 = 170772160.74
m2016 = 630278948.57
m2017 = 1747022829.31
m201801 = 208526348.00
mn201801 = 12219000

money_dict = {
    "2015": m2015,
    "2016": m2016,
    "2017": m2017,
    "201801": m201801

}

# for i in ss:
#     print(i)


# with open(r'E:\hoomsun_data\analysis\models\split_code.json', 'w') as j_file:
#     j_file.write(j)