from django.db import models
from django import forms

class basic(models.Model):  # 基本信息表
    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息'

    order_id = models.CharField('进件编号', max_length=30, primary_key=True)
    name = models.CharField('客户姓名', max_length=10, default='')
    # IDcard = models.CharField('身份证号', max_length=19, default='', blank=True)
    luruyuan = models.CharField('录入员', max_length=20, default='')

    type_list = (
        ('简版', '简版征信'),
        ('详版', '详版征信')
    )

    type = models.CharField('征信类型', max_length=6, choices=type_list, help_text='如为详版征信，选择详版征信后保存即可，无需录入详细信息')

    kongbai = models.BooleanField('征信空白', default=False)

    luru = models.BooleanField('录入完成', default=False)
    update_time = models.DateTimeField('更新时间', auto_now=True, blank=True)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)
    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    check_num = models.IntegerField('质检出错数目', null=True, default=0, blank=True)
    check_describe = models.TextField('质检备注', max_length=200, default='', blank=True)
    check_user = models.CharField('质检员编号', max_length=20, default='', blank=True)

    def __str__(self):
        return self.name


class summary(models.Model):  # 信息概要表
    class Meta:
        verbose_name = '信息概要'
        verbose_name_plural = '信息概要'
    order = models.ForeignKey(basic)
    query_date = models.DateField('征信报告时间', null=True, blank=True)
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

    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)

    def __str__(self):
        return '%s' % self.check_result


class card(models.Model):  # 信用卡信息表
    class Meta:
        verbose_name = '信用卡信息（最多添加30条, 只录人民币账户）'
        verbose_name_plural = '信用卡信息（最多添加30条, 只录人民币账户）'
    order = models.ForeignKey(basic)
    overdue = models.BooleanField('逾期', default=False)
    grant_date = models.DateField('发卡日期', null=True, blank=True)
    bank = models.CharField('发卡行', max_length=40, default='')
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
        ('未激活', '未激活'),
        ('冻结', '冻结'),
        ('呆账', '呆账'),
        ('降额', '降额'),
        ('止付', '止付'),
        ('其他', '其他')
    )
    account_state = models.CharField('账户状态', choices=state_list, max_length=10)
    five_years_overdue = models.IntegerField('近五年内逾期月数', null=True)
    ninety_days_overdue = models.IntegerField('90天以上逾期次数', null=True)
    overdue_money = models.FloatField('当前逾期金额', null=True)

    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)

    def __str__(self):
        return self.check_result

class loan(models.Model):  # 贷款信息表
    class Meta:
        verbose_name = '贷款信息（最多添加80条，不录贷款金额在500元以下贷款）'
        verbose_name_plural = '贷款信息（最多添加80条，不录贷款金额在500元以下贷款）'
    order = models.ForeignKey(basic)
    loan_type = (
        ('房贷', '房贷'),
        ('其他贷款', '其他贷款')

    )
    type = models.CharField('贷款类型', choices=loan_type, max_length=10)
    overdue = models.BooleanField('逾期', default=False)
    grant_date = models.DateField('发放日期', null=True, blank=True)
    institution = models.CharField('发放机构', max_length=40, default='')
    money = models.FloatField('发放金额', null=True)
    account_category_list = (
        ('个人住房贷款', '个人住房贷款'),
        ('个人公积金住房贷款', '个人公积金住房贷款'),
        ('个人消费贷款', '个人消费贷款'),
        ('个人经营贷款', '个人经营贷款'),
        ('个人信用贷款', '个人信用贷款'),
        ('农户贷款', '农户贷款'),
        ('个人汽车贷款', '个人汽车贷款'),
        ('住房抵押贷款', '住房抵押贷款'),
        ('汽车抵押贷款', '汽车抵押贷款'),
        ('抵押担保贷款', '抵押担保贷款'),
        ('其他抵押贷款', '其他抵押贷款'),
        ('装修贷款', '装修贷款'),
        ('助学贷款', '助学贷款'),
        ('其他贷款', '其他贷款')

    )
    account_category_main = models.CharField('贷款用途', choices=account_category_list, max_length=30, blank=True)
    account_category = models.CharField('其他贷款备注', max_length=40, default='如前面贷款用途不能涵盖则填写', blank=True, help_text='如果贷款用途选了其他贷款，请填写此项，否则无需填写')
    expired_date = models.DateField('到期日期', null=True)
    query_date = models.DateField('截止日期', null=True)
    figure = models.FloatField('余额', null=True)
    loan_state_list = (
        ('正常', '正常'),
        ('逾期', '逾期'),
        ('结清', '结清'),
        ('转出', '转出'),
        ('呆账', '呆账'),
        ('其他', '其他')

    )
    loan_state = models.CharField('贷款状态', choices=loan_state_list, max_length=10)
    yuqi_money = models.FloatField('逾期金额', null=True)
    years5_overdue = models.IntegerField('近五年内逾期月数', null=True)
    days90_overdue = models.IntegerField('90天以上逾期次数', null=True)
    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)
    def __str__(self):
        return self.check_result

class guarantee(models.Model):  # 担保信息表
    class Meta:
        verbose_name = '担保信息（最多添加20条）'
        verbose_name_plural = '担保信息（最多添加20条）'
    order = models.ForeignKey(basic)
    grant_date = models.DateField('起始日期', null=True)
    name_loan= models.CharField('被担保人', default='', max_length=20)
    card_loan = models.CharField('证件号后四位', max_length=10, default='')
    institution = models.CharField('贷款发放机构', max_length=80, default='')
    money = models.FloatField('担保合同金额', null=True)
    money2 = models.FloatField('担保金额', null=True)
    query_date = models.DateField('截止日期', null=True)
    figure = models.FloatField('余额', null=True)
    loan_state_list = (
        ('正常', '正常'),
        ('逾期', '逾期'),
        ('结清', '结清'),
        ('转出', '转出'),
        ('呆账', '呆账'),
        ('其他', '其他')

    )
    loan_state = models.CharField('贷款状态', choices=loan_state_list, max_length=10)
    yuqi_money = models.FloatField('逾期金额', null=True)

    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)
    def __str__(self):
        return self.check_result

class ggjl(models.Model):   # 公共记录
    class Meta:
        verbose_name = '公共记录'
        verbose_name_plural = '公共记录'
    order = models.ForeignKey(basic)
    public_record = models.TextField('公共记录', default='无', blank=True, max_length=2000)

    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)
    def __str__(self):
        return '%s' % self.check_result

class chaxun1(models.Model):  # 机构查询记录表
    class Meta:
        verbose_name = '征信查询-机构(最多添加50条)'
        verbose_name_plural = '征信查询-机构(最多添加50条)'
    order = models.ForeignKey(basic)
    chaxun_date = models.DateField('查询日期', null=True)
    caozuoyuan = models.CharField('查询操作员', default='', max_length=50)
    reason_list = (
        ('贷后管理', '贷后管理'),
        ('信用卡审批', '信用卡审批'),
        ('贷款审批', '贷款审批'),
        ('资信审查', '资信审查'),
        ('担保资格审查', '担保资格审查'),
        ('特约商户实名审查', '特约商户实名审查'),
        ('保前审查', '保前审查'),
        ('保后管理', '保后管理'),
        ('准入资格审查', '准入资格审查'),
        ('公积金提取复核', '公积金提取复核'),
        ('其他', '其他')

    )
    reason = models.CharField('查询原因', choices=reason_list, max_length=20)

    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)
    def __str__(self):
        return '%s' % self.check_result

class chaxun2(models.Model):  # 个人查询记录表
    class Meta:
        verbose_name = '征信查询-个人(最多添加50条)'
        verbose_name_plural = '征信查询-个人(最多添加50条)'
    order = models.ForeignKey(basic)
    chaxun_date = models.DateField('查询日期', null=True)
    reason_list = (
        ('个人临柜查询', '个人临柜查询'),
        ('个人互联网查询', '个人互联网查询')
    )
    reason = models.CharField('查询原因', choices=reason_list, max_length=20)

    check_list = (
        ('未质检', '未质检'),
        ('质检合格', '质检合格'),
        ('质检不合格', '质检不合格'),
        ('质检中', '质检中')

    )
    check_result = models.CharField('质检状态', choices=check_list, default='未质检', blank=True, max_length=20)
    update_time_ini = models.DateTimeField('创建时间', auto_now_add=True, blank=True)
    def __str__(self):
        return '%s' % self.check_result



