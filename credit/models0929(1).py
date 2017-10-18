from django.db import models


class card_detailed(models.Model):  # 信用卡信息-详
    class Meta:
        verbose_name = '信用卡信息-详'
        verbose_name_plural = '信用卡信息-详'
    card_id = models.AutoField('信用卡ID', primary_key=True)
    order = models.ForeignKey(basic)
    bank = models.CharField('发卡行', max_length=20, default='')
    grant_date = models.DateField('发卡日期', null=True)
    card_type_list = (
        ('贷记卡', '贷记卡'),
        ('信用卡', '信用卡'),
        ('准贷记卡', '准贷记卡')

    )
    account_category = models.CharField('卡类型', choices=card_type_list, max_length=10)
    state_list = (
        ('正常', '正常'),
        ('销户', '销户'),
        ('未激活', '未激活')
    )
    account_state = models.CharField('账户状态', choices=state_list, max_length=10)
    credit_Line = models.FloatField('信用额度', null=True)
    used_line = models.FloatField('已用额度', null=True)
    upto_date = models.DateField('截至日期', null=True)
    aver6_used_line = models.FloatField('最近6个月平均使用额度', null=True)
    max_used_line = models.FloatField('最大使用额度', null=True)
    month_should = models.FloatField('本月应还', null=True)
    bill_day = models.DateField('账单日', null=True)
    repayment_month = models.FloatField('本月实还款', null=True)
    last_repayment_date = models.DateField('最后一次还款日期', null=True)
    overdue_number_now = models.IntegerField('当前逾期期数', null=True)
    overdue_money_now = models.FloatField('当前逾期金额', null=True)


    def __str__(self):
        return self.bank


class loan_detailed(models.Model):  # 贷款信息-详
    class Meta:
        verbose_name = '贷款信息-详'
        verbose_name_plural = '贷款信息-详'
    loan_id = models.AutoField('贷款ID', primary_key=True)
    order = models.ForeignKey(basic)
    institution = models.CharField('发放机构', max_length=20, default='')
    grant_date = models.DateField('发放日期', null=True)
    money = models.FloatField('发放金额', null=True)
    loan_type = (
        ('房贷', '房贷'),
        ('其他贷款', '其他贷款')

    )
    type = models.CharField('贷款类型', choices=loan_type, max_length=10)
    revert_list = (
        ('按月归还', '按月归还'),
        ('一次性归还', '一次性归还')
    )
    revert = models.CharField('归还方式', choices=revert_list, max_length=10)
    expiration_date = models.DateField('到期日期', null=True)
    upto_date = models.DateField('截至日期', null=True)
    loan_state_list = (
        ('正常', '正常'),
        ('结清', '结清')
    )
    loan_state = models.CharField('账户状态', choices=loan_state_list, max_length=10)
    five_list = (
        ('正常', '正常'),
        ('关注', '关注'),
        ('次级', '次级'),
        ('可疑', '可疑'),
        ('损失', '损失')
    )
    five_classification = models.CharField('五级分类', choices=five_list, max_length=10)
    principal = models.FloatField('本金金额', null=True)
    remaining_number = models.IntegerField('剩余还款期数', null=True)
    reimbursement_should = models.FloatField('本月应还款', null=True)
    reimbursement_day = models.DateField('应还款日', null=True)
    reimbursement_reality = models.FloatField('本月实还款', null=True)
    recently_date = models.DateField('最近一次还款日期', null=True)
    overdue_number_now = models.IntegerField('当前逾期期数', null=True)
    overdue_money_now = models.FloatField('当前逾期金额', null=True)
    overdue31_60 = models.FloatField('逾期31-60天未还本金', null=True)
    overdue61_90 = models.FloatField('逾期61-90天未还本金', null=True)
    overdue91_180 = models.FloatField('逾期91-180天未还本金', null=True)
    overdue180 = models.FloatField('逾期180天以上未还本金', null=True)


    def __str__(self):
        return self.institution


class credit_summary(models.Model):  # 信用汇总表
    class Meta:
        verbose_name = '信用汇总'
        verbose_name_plural = '信用汇总'
    credit_summary_id = models.AutoField('信用汇总ID', primary_key=True)
    order = models.ForeignKey(basic)
    housing_loan_account = models.IntegerField('个人住房贷款笔数', null=True)
    housing_loan_commercial = models.IntegerField('个人商用房贷款笔数', null=True)
    other_loan_account = models.IntegerField('其他贷款笔数', null=True)
    first_loan_date = models.DateField('首笔贷款发放月份', null=True)
    credit_card_account = models.IntegerField('贷记卡账户数', null=True)
    first_credit_card = models.DateField('首张贷记卡发卡月份', null=True)
    quasi_credit_card = models.IntegerField('准贷记卡账户数', null=True)
    first_quasi_credit = models.DateField('首张准贷记卡发卡月份', null=True)
    statement_number = models.IntegerField('本人声明数目', null=True)
    objection_number = models.IntegerField('异议标注数目', null=True)

    def __str__(self):
        return self.housing_loan_account


class overdue(models.Model):  # 逾期信息汇总表
    class Meta:
        verbose_name = '逾期信息汇总'
        verbose_name_plural = '逾期信息汇总'
    overdue_id = models.AutoField('逾期汇总ID', primary_key=True)
    order = models.ForeignKey(basic)
    loan_overdue = models.IntegerField('贷款逾期笔数', null=True)
    loan_overdue_month = models.DateField('贷款逾期月分数', null=True)
    loan_overdue_most = models.FloatField('贷款逾期单月最高逾期总额', null=True)
    loan_overdue_longest = models.IntegerField('贷款逾期最长逾期月数', null=True)
    card_account = models.IntegerField('贷记卡逾期账户数', null=True)
    card_overdue_month = models.DateField('贷记卡逾期月分数', null=True)
    card_overdue_most = models.FloatField('贷记卡逾期单月最高逾期总额', null=True)
    card_overdue_longest = models.IntegerField('贷记卡逾期最长逾期月数', null=True)
    quasi_60_account = models.IntegerField('准贷记卡60天以上透支账户数', null=True)
    quasi_60_month = models.DateField('准贷记卡60天以上透支月分数', null=True)
    quasi_60_most = models.FloatField('准贷记卡60天以上透支单月最高透支余额', null=True)
    quasi_60_longest = models.IntegerField('准贷记卡60天以上透支最长透支月数', null=True)

    def __str__(self):
        return self.loan_overdue


class loan_summary(models.Model):  # 未结清贷款信息汇总
    class Meta:
        verbose_name = '未结清贷款信息汇总'
        verbose_name_plural = '未结清贷款信息汇总'
    loan_id = models.AutoField('贷款汇总ID', primary_key=True)
    order = models.ForeignKey(basic)
    loan_legal = models.IntegerField('贷款法人机构数', null=True)
    loan_institution = models.IntegerField('贷款机构数', null=True)
    number = models.IntegerField('笔数', null=True)
    contract_total = models.FloatField('合同总额', null=True)
    balance = models.FloatField('余额', null=True)
    average_6month = models.FloatField('最近6个月平均应还款', null=True)

    def __str__(self):
        return self.loan_legal


class card_summary(models.Model):  # 未销户贷记卡信息汇总
    class Meta:
        verbose_name = '未销户贷记卡信息汇总'
        verbose_name_plural = '未销户贷记卡信息汇总'
    card_summary_id = models.AutoField('贷记卡汇总ID', primary_key=True)
    order = models.ForeignKey(basic)
    card_legal = models.IntegerField('发卡法人机构数', null=True)
    card_institution = models.IntegerField('发卡机构数', null=True)
    account = models.IntegerField('账户数', null=True)
    credit_total = models.FloatField('授信总额', null=True)
    bank_most = models.FloatField('单家行最高授信额', null=True)
    bank_least = models.FloatField('单家行最低授信额', null=True)
    average_6month = models.FloatField('最近6个月平均使用额度', null=True)

    def __str__(self):
        return self.card_legal

class epayment_card_2years(models.Model):  # 近两年信用卡还款记录
    class Meta:
        verbose_name = '近两年信用卡还款记录'
        verbose_name_plural = '近两年信用卡还款记录'
    repayment_id = models.AutoField('还款记录ID', primary_key=True)
    order = models.ForeignKey(basic)
    y1 = models.IntegerField('N-23', null=True)
    y2 = models.IntegerField('N-22', null=True)
    y3 = models.IntegerField('N-21', null=True)
    y4 = models.IntegerField('N-20', null=True)
    y5 = models.IntegerField('N-19', null=True)
    y6 = models.IntegerField('N-18', null=True)
    y7 = models.IntegerField('N-17', null=True)
    y8 = models.IntegerField('N-16', null=True)
    y9 = models.IntegerField('N-15', null=True)
    y10 = models.IntegerField('N-14', null=True)
    y11 = models.IntegerField('N-13', null=True)
    y12 = models.IntegerField('N-12', null=True)
    y13 = models.IntegerField('N-11', null=True)
    y14 = models.IntegerField('N-10', null=True)
    y15 = models.IntegerField('N-9', null=True)
    y16 = models.IntegerField('N-8', null=True)
    y17 = models.IntegerField('N-7', null=True)
    y18 = models.IntegerField('N-6', null=True)
    y19 = models.IntegerField('N-5', null=True)
    y20 = models.IntegerField('N-4', null=True)
    y21 = models.IntegerField('N-3', null=True)
    y22 = models.IntegerField('N-2', null=True)
    y23 = models.IntegerField('N-1', null=True)
    y24 = models.IntegerField('N', null=True)

    def __str__(self):
        return self.y1


class epayment_loan_2years(models.Model):  # 近两年贷款还款记录
    class Meta:
        verbose_name = '近两年贷款还款记录'
        verbose_name_plural = '近两年贷款还款记录'
    repayment_id = models.AutoField('还款记录ID', primary_key=True)
    order = models.ForeignKey(basic)
    y1 = models.IntegerField('N-23', null=True)
    y2 = models.IntegerField('N-22', null=True)
    y3 = models.IntegerField('N-21', null=True)
    y4 = models.IntegerField('N-20', null=True)
    y5 = models.IntegerField('N-19', null=True)
    y6 = models.IntegerField('N-18', null=True)
    y7 = models.IntegerField('N-17', null=True)
    y8 = models.IntegerField('N-16', null=True)
    y9 = models.IntegerField('N-15', null=True)
    y10 = models.IntegerField('N-14', null=True)
    y11 = models.IntegerField('N-13', null=True)
    y12 = models.IntegerField('N-12', null=True)
    y13 = models.IntegerField('N-11', null=True)
    y14 = models.IntegerField('N-10', null=True)
    y15 = models.IntegerField('N-9', null=True)
    y16 = models.IntegerField('N-8', null=True)
    y17 = models.IntegerField('N-7', null=True)
    y18 = models.IntegerField('N-6', null=True)
    y19 = models.IntegerField('N-5', null=True)
    y20 = models.IntegerField('N-4', null=True)
    y21 = models.IntegerField('N-3', null=True)
    y22 = models.IntegerField('N-2', null=True)
    y23 = models.IntegerField('N-1', null=True)
    y24 = models.IntegerField('N', null=True)

    def __str__(self):
        return self.y1













