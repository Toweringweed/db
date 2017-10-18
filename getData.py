import pymysql
import pandas as pd

conn = pymysql.connect(host='192.168.1.178', port=3307, user ='root', passwd ='root', db = 'xindai20171012', charset ='utf8')
sql = r"SELECT ZKBC_CD_OPINION_SHOW_PRIMARY.LOANID, ZKBC_CD_OPINION_SHOW_TRIAL.LOAN_DATA_ANALY, " \
       r"ZKBC_CD_OPINION_SHOW_TRIAL.CREDIT_INFO_EVALUATE, ZKBC_CD_OPINION_SHOW_TRIAL.TRIAL_INNER_OPINION, " \
       r"ZKBC_CD_OPINION_SHOW_TRIAL.TRIAL_PRIMARY_OPINION_VAL FROM ZKBC_CD_OPINION_SHOW_PRIMARY " \
       r"left join ZKBC_CD_OPINION_SHOW_TRIAL " \
       r"on ZKBC_CD_OPINION_SHOW_PRIMARY.OSP_PK_ID = ZKBC_CD_OPINION_SHOW_TRIAL.OSP_PK_ID; "
df = pd.read_sql(sql, conn)

save_path = r'E:\txt_data.csv'
pd.DataFrame.to_csv(df, save_path, sep=',', index=None)




