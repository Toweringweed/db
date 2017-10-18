
时间
1、gt：大于某个时间
now = datetime.datetime.now()
#前一天
start = now – datetime.timedelta(hours=23, minutes=59, seconds=59)
a=yourobject.objects .filter(youdatetimcolumn__gt=start)

2、gte：大于等于某个时间：
a=yourobject.objects .filter(youdatetimcolumn__gte=start)

3、lt：小于
a=yourobject.objects .filter(youdatetimcolumn__lt=start)

4、lte：小于等于
a=yourobject.objects .filter(youdatetimcolumn__lte=start)

5、range：查询时间段
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))

6、year：查询某年
Entry.objects.filter(pub_date__year=2005)

7、month：查询某月
Entry.objects.filter(pub_date__month=12)

8、day：某天
Entry.objects.filter(pub_date__day=3)

9、week_day：星期几
Entry.objects.filter(pub_date__week_day=2)

10、获取今天的日期，日期格式为yyyy-MM-dd

from django.utils.timezone import now, timedelta
date = now().date() + timedelta(days=-1) #昨天
date = now().date() + timedelta(days=0) #今天
date = now().date() + timedelta(days=1) #明天