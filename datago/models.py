from django.db import models

class customer(models.Model):  # 借款人概况表
    customer_id = models.CharField('客户编号', primary_key=True, max_length=30)
    customer_name = models.CharField('客户姓名', max_length=20, default='')
    Idcard = models.CharField('身份证号', max_length=19, unique=True)
    sex = models.CharField('性别', max_length=2, default='')
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.customer_name

class product(models.Model):
    product_id = models.CharField('产品编号', max_length=10, primary_key=True)
    product_name = models.CharField('产品名称', max_length=20, default='')
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.product_name

class product_month(models.Model):
    product_month_id = models.CharField('产品期限编号', primary_key=True, max_length=10)
    product_month = models.IntegerField('产品期限', null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.product_month

class company(models.Model):
    company_id = models.CharField('事业部编号', max_length=16, primary_key=True)
    company = models.CharField('事业部名称', max_length=20)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.company

class region(models.Model):
    region_id = models.CharField('区域编号', max_length=16, primary_key=True)
    region = models.CharField('区域名称', max_length=20)
    company = models.ForeignKey(company)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.region

class city(models.Model):
    city_id = models.CharField('城市编号', max_length=10, primary_key=True)
    city = models.CharField('城市名称', max_length=20, default='')
    region = models.ForeignKey(region)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.city

class department(models.Model):
    department_id = models.CharField('机构编号', max_length=10, primary_key=True)
    department = models.CharField('机构名称', max_length=50, default='')
    city = models.ForeignKey(city)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.department

class employee(models.Model):
    employee_id = models.CharField('员工编号', max_length=10, primary_key=True)
    employee_name = models.CharField('员工姓名', max_length=20, default='')
    active_service = models.CharField('在职状态', max_length=10, default='')
    department = models.ForeignKey(department)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.employee_name

class employee_tran(models.Model):
    id = models.AutoField('id', primary_key=True)
    employee = models.ForeignKey(employee)
    active_position = models.CharField('职务', max_length=10, default='')
    trans_start = models.DateField('起始时间', null=True, blank=True)
    trans_end = models.DateField('结束时间', null=True, blank=True)
    department = models.ForeignKey(department)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.active_position

class orders(models.Model):  # 订单表
    order_id = models.CharField('订单流水号', max_length=50, primary_key=True)
    order_date = models.DateField('订单日期', null=True, blank=True)
    product = models.ForeignKey(product)
    product_month = models.ForeignKey(product_month)
    customer = models.ForeignKey(customer)
    type = models.CharField('线上/线下', max_length=10, blank=True, default='')
    money_apply = models.IntegerField('申请金额', null=True, blank=True)
    marketing_channel = models.CharField('销售渠道', max_length=20, default='', blank=True)
    customer_source = models.CharField('客户来源', max_length=20, default='', blank=True)
    urgent = models.CharField('紧急程度', max_length=20, default='', blank=True)
    money_verify_first = models.DecimalField('初审金额', max_digits=12, decimal_places=2, null=True, blank=True)
    enterprise_credit = models.CharField('工商网信息', max_length=20, default='', blank=True)
    enterprise_credit_bz = models.CharField('工商网信息备注', max_length=300, default='', blank=True)
    court = models.CharField('法院网信息', max_length=400, default='', blank=True)
    address_proven = models.CharField('是否有住址证明', max_length=10, default='', blank=True)
    address_proven_bz = models.CharField('住址证明备注', max_length=200, default='', blank=True)
    private_owner = models.BooleanField('是否私营业主', default=False, blank=True)
    continues = models.BooleanField('是否续借', default=False, blank=True)
    verify_income_initial = models.DecimalField('核实收入金额(初审)', max_digits=12, decimal_places=2, null=True, blank=True)
    verify_indebted_initial = models.DecimalField('核实负债金额(初审)', max_digits=12, decimal_places=2, null=True, blank=True)
    verify_money_initial = models.DecimalField('理论审批金额(初审)', max_digits=12, decimal_places=2, null=True, blank=True)
    debt_ratio_initial = models.DecimalField('信用负债率(初审)', max_digits=8, decimal_places=2, null=True, blank=True)
    opinion_initial = models.CharField('初审内部意见', max_length=500, default='')
    material_evaluation = models.CharField('贷款资料评估', max_length=500, default='')
    credit_evaluation = models.CharField('信用信息评估', max_length=500, default= '')
    risk = models.CharField('信用风险点', max_length=2000, default='')
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.order_id

class education(models.Model):  # 借款人学历表
    id = models.AutoField('学历编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    education = models.CharField('学历', max_length=15, default='', blank=True)
    college = models.CharField('毕业院校', max_length=60, default='', blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.education

class hukou(models.Model):   # 户口表
    id = models.AutoField('户口编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    home_province = models.CharField('户口所在省', max_length=20, default='', blank=True)
    home_city = models.CharField('户口所在市', max_length=20, default='', blank=True)
    home_district = models.CharField('户口所在区', max_length=30, default='', blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.home_city

class reside(models.Model):  #借款人居住情况表
    id = models.AutoField('居住编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    reside_time = models.DateField('起始居住时间', null=True, blank=True)
    reside_conditions = models.CharField('居住状况', max_length=10, default='')
    rent = models.DecimalField('租金月还', max_digits=8, decimal_places=2, null=True, blank=True)
    reside_province = models.CharField('住宅所在省', max_length=20, default='')
    reside_city = models.CharField('住宅所在市', max_length=20, default='')
    reside_district = models.CharField('住宅所在区', max_length=30, default='')
    arrival_time = models.DateField('来本地年份', null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.reside_conditions

class occupation(models.Model):  # 借款人职业表
    id = models.AutoField('职业编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    company = models.CharField('单位名称', max_length=50, default='')
    service_time = models.DateField('起始服务时间', null=True, blank=True)
    positions = models.CharField('职务名称', max_length=20, default='', blank=True)
    levels = models.CharField('职务级别', max_length=20, default='', blank=True)
    department = models.CharField('所属部门', max_length=20, default='', blank=True)
    industry = models.CharField('所属行业', max_length=30, default='', blank=True)
    category = models.CharField('单位性质', max_length=20, default='', blank=True)
    pay = models.CharField('发薪方式', max_length=10, default='', blank=True)
    scope = models.CharField('公司规模', max_length=10, default='', blank=True)
    social_security = models.CharField('社保情况', max_length=10, default='', blank=True)
    company_province = models.CharField('单位地址（省）', max_length=20, default='', blank=True)
    company_city = models.CharField('单位地址（市）', max_length=20, default='', blank=True)
    company_district = models.CharField('单位地址（区）', max_length=30, default='', blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    def __str__(self):
        return self.company

class household(models.Model):  # 借款人家庭表
    id = models.AutoField('家庭编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    marital_status = models.CharField('婚姻情况', max_length=10, default='')
    support = models.IntegerField('供养人数', null=True, blank=True)
    children = models.IntegerField('子女数目', null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.marital_status

class car(models.Model):   # 借款人车产表  //
    id = models.AutoField('车产编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    car_category = models.CharField('车产类别', max_length=10, default='')
    car_price = models.IntegerField('购买价格', null=True, blank=True)
    car_age = models.IntegerField('车龄', null=True, blank=True)
    car_loan_date = models.DateField('贷款发放日期', null=True, blank=True)
    mortgage_monthly = models.DecimalField('按揭月供', max_digits=8, decimal_places=2, null=True, blank=True)
    loan_total = models.DecimalField('贷款总额', max_digits = 10, decimal_places=2, null=True, blank=True)
    car_Remaining_date = models.IntegerField('剩余期限', null=True, blank=True)
    car_balance_amount = models.DecimalField('贷款余额', max_digits = 10, decimal_places=2, null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.car_price

class house(models.Model):   # 房产表
    id = models.AutoField('房产编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    house_category = models.CharField('房产类别', max_length=10, default='')
    house_loan_monthly = models.DecimalField('房贷月还', max_digits = 8, decimal_places=2, null=True, blank=True)
    purchase_time = models.DateField('购买时间', null=True, blank=True)
    house_price = models.DecimalField('购买价格', max_digits = 10, decimal_places=2, null=True, blank=True)
    purchase_area = models.DecimalField('建筑面积', max_digits = 15, decimal_places=2, null=True, blank=True)
    possession = models.CharField('房产所属', max_length=10, default='')
    relation = models.CharField('共有人关系', max_length=10, default='')
    time_limit = models.IntegerField('借款年限', null=True, blank=True)
    house_Remaining_date = models.IntegerField('剩余期限', null=True, blank=True)
    sameness = models.BooleanField('住宅与地址是否相同')
    house_balance_amount = models.DecimalField('贷款余额', max_digits= 10, decimal_places=2, null=True, blank=True)
    house_province = models.CharField('住宅所在省', max_length=20, default='')
    house_city = models.CharField('住宅所在市', max_length=20, default='')
    house_district = models.CharField('住宅所在区', max_length=30, default='')
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.house_category

class shouru(models.Model):  # 手填收入   //
    id = models.AutoField('收入编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    salary = models.IntegerField('每月基本薪金(自填)', null=True, blank=True)
    other_income = models.IntegerField('其他收入(自填)', null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.salary

class income(models.Model):  # 银行流水
    income_id = models.AutoField('银行流水编号', max_length=30, primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    bank_in1 = models.DecimalField('银行流水第一个月(合计)', max_digits = 12, decimal_places=2, null=True, blank=True)
    bank_in2 = models.DecimalField('银行流水第二个月(合计)', max_digits = 12, decimal_places=2, null=True, blank=True)
    bank_in3 = models.DecimalField('银行流水第三个月(合计)', max_digits = 12, decimal_places=2, null=True, blank=True)
    bank_in4 = models.DecimalField('银行流水第四个月(合计)', max_digits = 12, decimal_places=2, null=True, blank=True)
    bank_in5 = models.DecimalField('银行流水第五个月(合计)', max_digits = 12, decimal_places=2, null=True, blank=True)
    bank_in6 = models.DecimalField('银行流水第六个月(合计)', max_digits = 12, decimal_places=2, null=True, blank=True)
    income_type = models.CharField('流水类型', max_length=10, default='', blank=True)
    income_habit = models.CharField('花费习惯', max_length=20, default='', blank=True)
    bank_mean = models.DecimalField('流水平均值', max_digits=13, decimal_places=3, null=True, blank=True)
    bank_std = models.DecimalField('流水标准差', max_digits=13, decimal_places=3, null=True, blank=True)
    bank_var = models.DecimalField('流水变异系数', max_digits=8, decimal_places=3, null=True, blank=True)
    bank_jiexi1 = models.DecimalField('结息1', max_digits=13, decimal_places=3, null=True, blank=True)
    bank_jiexi2 = models.DecimalField('结息2', max_digits=13, decimal_places=3, null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.bank_mean

class insure(models.Model):
    id = models.AutoField('社保编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    insured_months = models.IntegerField('连续投保月数', null=True, blank=True)
    insurance_money = models.DecimalField('社保金额', max_digits=10, decimal_places=2, null=True, blank=True)
    fund_months = models.IntegerField('连续缴纳公积金月数')
    fund_money = models.DecimalField('公积金缴纳金额', max_digits=10, decimal_places=2, null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.insurance_money

class lending(models.Model):   #////
    id = models.AutoField('借贷编号', primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    repayment_monthly_house = models.DecimalField('抵押房产月供款(每月供款)', max_digits = 12, decimal_places=2, null=True, blank=True)
    repayment_monthly_car = models.DecimalField('抵押汽车月供款(每月供款)', max_digits = 12, decimal_places=2, null=True, blank=True)
    repayment_monthly_business = models.DecimalField('经营性贷款月供款(每月供款)', max_digits = 12, decimal_places=2, null=True, blank=True)
    repayment_monthly_credit = models.DecimalField('信用型贷款月供款(每月供款)', max_digits = 12, decimal_places=2, null=True, blank=True)
    repayment_monthly_hide = models.DecimalField('隐性负债月贷款(每月供款)', max_digits = 12, decimal_places=2, null=True, blank=True)
    number_housing_loan = models.IntegerField('房贷总笔数',null=True, blank=True)
    settle_housing_loan = models.IntegerField('房贷结清笔数', null=True, blank=True)
    M2_housing_loan = models.IntegerField('房贷(M2次数)', null=True, blank=True)
    M1_housing_loan = models.IntegerField('房贷(M1次数)', null=True, blank=True)
    number_car_loan = models.IntegerField('车贷总笔数', null=True, blank=True)
    settle_car_loan = models.IntegerField('车贷结清笔数', null=True, blank=True)
    M2_car_loan = models.IntegerField('车贷(M2次数)', null=True, blank=True)
    M1_car_loan = models.IntegerField('车贷(M1次数)', null=True, blank=True)
    expiry = models.BooleanField('信用是否逾期')
    expiry_day = models.IntegerField('贷款逾期天数', null=True, blank=True)
    total_sum = models.DecimalField('总信用额度', max_digits = 12, decimal_places=2, null=True, blank=True)
    total_use = models.DecimalField('已使用额度', max_digits = 12, decimal_places=2, null=True, blank=True)
    indebted_sum = models.DecimalField('最大负债和', max_digits = 12, decimal_places=2, null=True, blank=True)
    card_sum = models.IntegerField('总张数', null=True, blank=True)
    card_normal = models.IntegerField('正常张数', null=True, blank=True)
    M2_card = models.IntegerField('M2次数', null=True, blank=True)
    M1_card = models.IntegerField('M1次数', null=True, blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.repayment_monthly_house

class contract(models.Model):
    contract_id = models.CharField('合同编号', max_length=50, primary_key=True)
    customer = models.ForeignKey(customer)
    order_id = models.CharField('订单编号', max_length=30, default='', blank=True)
    contract_date = models.DateTimeField('签约日期')
    contract_money = models.DecimalField('合同金额', max_digits=12, decimal_places=2)
    approved_money = models.DecimalField('放款金额',  max_digits=12, decimal_places=2)
    product = models.ForeignKey(product)
    rate = models.DecimalField('利率', max_digits=8, decimal_places=3, null=True, blank=True)
    loan_date = models.DateTimeField('放款日期', null=True, blank=True)
    repay_date_start = models.DateField('还款起始日期', null=True, blank=True)
    repay_date_end = models.DateField('还款到期日期', null=True, blank=True)
    loan_monthly = models.DecimalField('月还款额', max_digits=10, decimal_places=2)
    bank_name = models.CharField('银行名称', max_length=30, default='', null=True, blank=True)
    bank_account = models.CharField('银行账号', max_length=30, default='', null=True, blank=True)
    contract_type = models.CharField('合同类型', max_length=10, default='', null=True, blank=True)
    online = models.CharField('线上/线下', max_length=10, default='', blank=True)
    pos = models.CharField('POS认证', max_length=10, default='', blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.contract_money

class repay(models.Model):
    contract = models.OneToOneField(contract)
    customer = models.ForeignKey(customer)
    settle = models.BooleanField('是否结清', default=False)
    preact = models.BooleanField('是否提前还款', default=False)
    last_date = models.DateTimeField('最后还款日期', null=True, blank=True)
    repay_overdue = models.BooleanField('是否有当前逾期', default=False)
    repay_overdue_his = models.BooleanField('是否有历史逾期', default=False)
    repay_qici = models.IntegerField('当期期次', null=True)
    yuqi_number = models.IntegerField('累计逾期期次', null=True)
    over_days = models.IntegerField('逾期天数', null=True, blank=True)

    def __str__(self):
        return self.repay_qici

class repayment(models.Model):
    repayment_id = models.CharField('还款编号', max_length=60, primary_key=True)
    contract_id = models.CharField('合同编号', max_length=40, default='')
    customer_name = models.CharField('客户姓名', max_length=20, default='', blank=True)
    bank_account = models.CharField('还款银行账号', max_length=30, default='')
    residual_money = models.DecimalField('期初剩余本金', max_digits=12, decimal_places=2)
    residual_money2 = models.DecimalField('计算期初剩余本金）', max_digits=12, decimal_places=2)
    period = models.IntegerField('当期期次')
    product_month = models.ForeignKey(product_month)
    repay_date = models.DateTimeField('报表日期', null=True, blank=True)
    should_date = models.DateTimeField('应还日期', null=True, blank=True)
    actual_date = models.DateTimeField('实际还款日期', null=True, blank=True)
    repay_condition = models.CharField('还款情况', max_length=30, default='')
    repay_month = models.DecimalField('月还款额', max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    repay_capital = models.DecimalField('归还本金', max_digits= 12, decimal_places=2, null=True, blank=True, default=0)
    repay_interest = models.DecimalField('归还利息', max_digits= 12, decimal_places=2, null=True, blank=True, default=0)
    repay_punish1 = models.DecimalField('应收违约金', max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    repay_punish2 = models.DecimalField('应收罚息', max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    repay_punish3 = models.DecimalField('应收违罚金', max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    repay_sum = models.DecimalField('应收总额', max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    repay_in = models.DecimalField('已收金额', max_digits=12, decimal_places=2, null=True, blank=True)
    repay_owe = models.DecimalField('结欠金额', max_digits=12, decimal_places=2, null=True, blank=True)
    repay_reduce = models.DecimalField('减免金额', max_digits=12, decimal_places=2, null=True, blank=True)
    repay_overdue = models.BooleanField('是否逾期', default=False)
    yuqi_qici = models.IntegerField('累计逾期期次', default=0)
    type = models.CharField('表类型', default='', blank=True, max_length=10)
    online = models.CharField('线上/线下', default='', blank=True, max_length=10)
    pos = models.CharField('POS机', default='', blank=True, max_length=10)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.period

class repaywork(models.Model):
    contract = models.ForeignKey(contract)
    customer = models.ForeignKey(customer)
    department = models.ForeignKey(department)
    employee = models.ForeignKey(employee)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.employee


class order_t(models.Model):
    contract_id = models.CharField('合同编号', max_length=30, default='', primary_key=True)
    idcard = models.CharField('身份证号', max_length=20, default='', blank=True)
    customer_name = models.CharField('客户姓名', max_length=20, default='')
    region = models.ForeignKey(region)
    department = models.CharField('营业部名称', max_length=30, default='', primary_key=True)
    city = models.ForeignKey(city)
    city_sub = models.CharField('客户所在城市', max_length=30, default='', blank=True)
    result_chushen = models.CharField('初审结果', max_length=20, default='', blank=True)
    result_zhongshen = models.CharField('终审结果', max_length=20, default='', blank=True)
    date_chushen = models.DateField('初审日期', null=True)
    date_zhongshen = models.DateField('终审日期', null=True)
    product = models.ForeignKey(product)
    product_month = models.ForeignKey(product_month)
    money_chushen = models.IntegerField('初审金额', null=True, blank=True)
    money_pihe = models.IntegerField('批核金额', null=True, blank=True)
    tuihui = models.BooleanField('是否退回', default=False)
    fuyi = models.BooleanField('是否复议', default=False)
    shenpiyijian = models.CharField('审批意见', max_length=400, default='', blank=True)
    fangkuanbeizhu = models.CharField('备注', max_length=400, default='', blank=True)
    one_hour = models.BooleanField('1小时', default=False)
    two_hour = models.BooleanField('2小时', default=False)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.result_zhongshen

class contract_t(models.Model):
    contract_id = models.CharField('合同编号',primary_key=True, max_length=30, default='')
    idcard = models.CharField('身份证号', max_length=20, default='', blank=True)
    customer = models.ForeignKey(customer)
    customer_name = models.CharField('客户姓名', max_length=20, default='')
    bank_account = models.CharField('还款银行账号', max_length=30, default='', blank=True)
    region = models.ForeignKey(region)
    department = models.ForeignKey(department)
    city = models.ForeignKey(city)
    date_shencha = models.DateField('放款审查日期', null=True, blank=True)
    date_fangkuan = models.DateField('放款日期', null=True, blank=True)
    contract_date = models.DateField('签约日期', null=True, blank=True)
    result_shencha = models.CharField('放款审查结果', max_length=20, default='', blank=True)
    product = models.ForeignKey(product)
    product_month = models.ForeignKey(product_month)
    money_pihe = models.IntegerField('核批金额', null=True, blank=True)
    money_contract = models.DecimalField('合同金额', max_digits=12, decimal_places=2, null=True, blank=True)
    money_month = models.DecimalField('月还款额', max_digits=10, decimal_places=2, null=True, blank=True)
    qianyuetiaojian = models.CharField('签约条件', max_length=400, default='', blank=True)
    fangkuanbeizhu = models.CharField('放款备注', max_length=400, default='', blank=True)
    tuihuiyuanyin = models.CharField('退回原因', max_length=500, default='', blank=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.customer_name

class order_t_worker(models.Model):
    order = models.OneToOneField(order_t)
    department = models.ForeignKey(department)
    customer_manager = models.ForeignKey(employee, related_name='customer_manage_em')
    team_manager = models.ForeignKey(employee, related_name='team_manager_em')
    customer_service = models.ForeignKey(employee, related_name='customer_service_em')
    verify_first = models.ForeignKey(employee, related_name='verify_first_em')
    verify_final = models.ForeignKey(employee, related_name='verify_final_em')
    contract_service = models.ForeignKey(employee, related_name='contract_service_em')
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.order











