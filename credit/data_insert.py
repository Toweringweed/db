from personal.mysqldb import ToMysql
import pymysql
import pandas as pd
from dateutil.parser import parse
import numpy as np
import decimal
import re
import string
from datetime import datetime
import time

np.set_printoptions(threshold=100000)
pd.options.display.max_rows = 100000
pd.options.display.max_columns = 500
pd.set_option('expand_frame_repr', False)

kwargs = {'host': '114.55.30.247',
          'user': 'root',
          'passwd': 'LJRoOrnaWtG0',
          'db': 'credit_visual',
          'charset': 'utf8'}
sql = ToMysql(kwargs)

read_path = r'E:\hoomsun_data\数据源\loan_user_9.18.csv'
df = pd.read_csv(read_path, encoding='gbk', dtype='unicode')

for index, row in df.iterrows():
    credit_dict = {
        'order_id': row['LOANID'],
        'name': row['CUSTNAME'],
        'IDcard': row['PAPERID'],
        'adress': '',
        'luru': False,
        'type': 'jian',
        'kongbai': False

    }
    sql.into('credit_basic', **credit_dict)





