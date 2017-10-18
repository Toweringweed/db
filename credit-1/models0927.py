from django.db import models


class basic_information(models.Model):  # 基本信息表
    order_id = models.CharField('订单流水号', max_length=50, primary_key=True)
    name = models.CharField('客户姓名', max_length=20, default='')
    IDcard = models.CharField('身份证号', max_length=19, unique=True)
    

    def __str__(self):
        return self.name

class credit_card_information(models.Model):  # 信用卡信息表
    credit_card_id = models.AutoField('信用卡ID', primary_key=True)
    IDcard = models.CharField('身份证号', max_length=19, unique=True)
    bank = models.CharField('发卡行', max_length=20, default='')
    grant_date = models.DateField('发卡日期', null=True, blank=True)
    account_category = models.CharField('账户类别', max_length=10, default='')
    account_state = models.CharField('账户状态', max_length=10, default='')
    query_date = models.DateField('查询年月', null=True, blank=True)
    credit_Line = models.DecimalField('信用额度', max_digits=12, decimal_places=2, null=True, blank=True)
    used_line = models.DecimalField('已使用额度', max_digits=12, decimal_places=2, null=True, blank=True)
    overdue = models.BooleanField('是否逾期', default=False, blank=True)
    five_years_overdue = models.IntegerField('近五年内逾期月数', null=True, blank=True)
    ninety_days_overdue = models.IntegerField('90天以上逾期次数', null=True, blank=True)

    def __str__(self):
        return self.bank

class loan_information(models.Model):  # 贷款信息表
    loan_id = models.AutoField('贷款ID', primary_key=True)
    IDcard = models.CharField('身份证号', max_length=19, unique=True)
    institution = models.CharField('发放机构', max_length=20, default='')
    grant_date = models.DateField('发卡日期', null=True, blank=True)
    money = models.DecimalField('发放金额', max_digits=12, decimal_places=2, null=True, blank=True)
    account_category = models.CharField('账户类别', max_length=10, default='')
    expired_date = models.DateField('到期日期', null=True, blank=True)
    query_date = models.DateField('查询年月', null=True, blank=True)
    figure = models.DecimalField('余额', max_digits=12, decimal_places=2, null=True, blank=True)
    overdue = models.BooleanField('是否逾期', default=False, blank=True)
    five_years_overdue = models.IntegerField('近五年内逾期月数', null=True, blank=True)
    ninety_days_overdue = models.IntegerField('90天以上逾期次数', null=True, blank=True)

    def __str__(self):
        return self.institution
class query_log(models.Model):  # 查询记录表
    query_id = models.AutoField('贷款ID', primary_key=True)
    IDcard = models.CharField('身份证号', max_length=19, unique=True)
    query_date = models.DateField('查询年月', null=True, blank=True)
    thirtydays_personal_query = models.IntegerField('近30天个人查询次数', null=True, blank=True)
    thirtydays_institution_query = models.IntegerField('近30天机构查询次数', null=True, blank=True)
    thirtydays_manage_query = models.IntegerField('近30天贷后管理次数', null=True, blank=True)
    twomonths_personal_query = models.IntegerField('近2个月个人查询次数', null=True, blank=True)
    twomonths_institution_query = models.IntegerField('近2个月机构查询次数', null=True, blank=True)
    twomonths_manage_query = models.IntegerField('近2个月贷后管理次数', null=True, blank=True)
    sixmonths_personal_query = models.IntegerField('近6个月个人查询次数', null=True, blank=True)
    sixmonths_institution_query = models.IntegerField('近6个月机构查询次数', null=True, blank=True)
    sixmonths_manage_query = models.IntegerField('近6个月贷后管理次数', null=True, blank=True)

    def __str__(self):
        return self.Idcard







