from datetime import datetime, timedelta
import time
from django.http import JsonResponse
import json
from dateutil.parser import parse
from itertools import chain


today = datetime.today()
second = datetime.strptime('20171008', '%Y%m%d')
days = (today - second).days
print(days)

