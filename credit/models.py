from django.db import models
from django import forms

class basic(models.Model):  # 基本信息表
    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息'
    order_id = models.CharField('订单流水号', max_length=30, primary_key=True)
    name = models.CharField('客户姓名', max_length=10, default='')
    IDcard = models.CharField('身份证号', max_length=19, default='')
    adress = models.CharField('征信影印件', max_length=150)

    type_list = (
        ('简版', '简版征信'),
        ('详版', '详版征信')
    )
    type = models.CharField('征信类型', max_length=6, choices=type_list)

    kongbai = models.BooleanField('征信空白', default=False)
    luruyuan = models.CharField('录入员', default='', null=True, max_length=15)
    luru = models.BooleanField('录入完成', default=False)
    update_time = models.DateTimeField('更新时间', auto_now=True, blank=True)

    def __str__(self):
        return self.name


class summary(models.Model):  # 信息概要表
    class Meta:
        verbose_name = '信息概要'
        verbose_name_plural = '信息概要'
    order = models.ForeignKey(basic)
    query_date = models.DateField('查询日期', null=True)
    card_account = models.IntegerField('信用卡账户数', null=True)
    card_notsettled = models.IntegerField('信用卡未结清/未销户账户数', null=True)
    card_overdue = models.IntegerField('信用卡发生过逾期的账户数', null=True)
    card_90overdue = models.IntegerField('信用卡发生过90天以上逾期的账户数', null=True)
    card_guaranty = models.IntegerField('信用卡为他人担保笔数', null=True)
    housing_loan_account = models.IntegerField('购房贷款账户数', null=True)
    housing_loan_notsettled = models.IntegerField('购房贷款未结清/未销户账户数', null=True)
    housing_loan_overdue = models.IntegerField('购房贷款发生过逾期的账户数', null=True)
    housing_loan_90overdue = models.IntegerField('购房贷款发生过90天以上逾期的账户数', null=True)
    housing_loan_guaranty = models.IntegerField('购房贷款为他人担保笔数', null=True)
    other_loan_account = models.IntegerField('其他贷款账户数', null=True)
    other_loan_notsettled = models.IntegerField('其他贷款未结清/未销户账户数', null=True)
    other_loan_overdue = models.IntegerField('其他贷款发生过逾期的账户数', null=True)
    other_loan_90overdue = models.IntegerField('其他贷款发生过90天以上逾期的账户数', null=True)
    other_loan_guaranty = models.IntegerField('其他贷款为他人担保笔数', null=True)

    def __str__(self):
        return '%s' % self.card_account


class card(models.Model):  # 信用卡信息表
    class Meta:
        verbose_name = '信用卡信息（最多添加30条, 不录非人民币账户）'
        verbose_name_plural = '信用卡信息（最多添加30条, 不录非人民币账户）'
    order = models.ForeignKey(basic)
    overdue = models.BooleanField('逾期', default=False)
    grant_date = models.DateField('发卡日期', null=True, blank=True)
    bank = models.CharField('发卡行', max_length=20, default='')
    card_type_list = (
        ('贷记卡', '贷记卡'),
        ('信用卡', '信用卡'),
        ('准贷记卡', '准贷记卡')

    )
    account_category = models.CharField('卡类型', choices=card_type_list, max_length=10)
    query_date = models.DateField('截止日期', null=True, blank=True)
    credit_Line = models.FloatField('信用额度', null=True)
    used_line = models.FloatField('已使用额度', null=True)
    state_list = (
        ('正常', '正常'),
        ('销户', '销户'),
        ('未激活', '未激活')
    )
    account_state = models.CharField('账户状态', choices=state_list, max_length=10)
    five_years_overdue = models.IntegerField('近五年内逾期月数', null=True)
    ninety_days_overdue = models.IntegerField('90天以上逾期次数', null=True)
    overdue_money = models.FloatField('当前逾期金额', null=True)

    def __str__(self):
        return self.bank

class loan(models.Model):  # 贷款信息表
    class Meta:
        verbose_name = '贷款信息（最多添加30条，不录放款金额在5000元以下的贷款）'
        verbose_name_plural = '贷款信息（最多添加30条，不录放款金额在5000元以下的贷款）'
    order = models.ForeignKey(basic)
    loan_type = (
        ('房贷', '房贷'),
        ('其他贷款', '其他贷款')

    )
    type = models.CharField('贷款类型', choices=loan_type, max_length=10)
    overdue = models.BooleanField('逾期', default=False)
    grant_date = models.DateField('发放日期', null=True, blank=True)
    institution = models.CharField('发放机构', max_length=20, default='')
    money = models.FloatField('发放金额', null=True)
    account_category = models.CharField('贷款用途', max_length=10, default='')
    expired_date = models.DateField('到期日期', null=True)
    query_date = models.DateField('截止日期', null=True)
    figure = models.FloatField('余额', null=True)
    loan_state_list = (
        ('正常', '正常'),
        ('逾期', '逾期'),
        ('已结清', '已结清')
    )
    loan_state = models.CharField('贷款状态', choices=loan_state_list, max_length=10)
    yuqi_money = models.FloatField('逾期金额', null=True)
    years5_overdue = models.IntegerField('近五年内逾期月数', null=True)
    days90_overdue = models.IntegerField('90天以上逾期次数', null=True)

    def __str__(self):
        return self.institution

class chaxun1(models.Model):  # 机构查询记录表
    class Meta:
        verbose_name = '机构征信查询'
        verbose_name_plural = '机构征信查询'
    order = models.ForeignKey(basic)
    chaxun_date = models.DateField('查询日期', null=True, blank=True)
    caozuoyuan = models.CharField('查询操作员', default='', max_length=50)
    reason_list = (
        ('贷后管理', '贷后管理'),
        ('信用卡审批', '信用卡审批'),
        ('贷款审批', '贷款审批'),
        ('担保资格审查', '担保资格审查'),
        ('特约商户实名审查', '特约商户实名审查'),
        ('其他', '其他')

    )
    reason = models.CharField('查询原因', choices=reason_list, max_length=20)

    def __str__(self):
        return '%s' % self.reason

class chaxun2(models.Model):  # 个人查询记录表
    class Meta:
        verbose_name = '个人征信查询'
        verbose_name_plural = '个人征信查询'
    order = models.ForeignKey(basic)
    chaxun_date = models.DateField('查询日期', null=True, blank=True)
    reason_list = (
        ('个人临柜查询', '个人临柜查询'),
        ('个人互联网查询', '个人互联网查询'),
    )
    reason = models.CharField('查询原因', choices=reason_list, max_length=20)

    def __str__(self):
        return '%s' % self.reason



