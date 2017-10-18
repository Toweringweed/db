# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ZhbCdBorrowerInfo(models.Model):
    binfo_pk_id = models.CharField(db_column='BINFO_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loan_pk_id = models.CharField(db_column='LOAN_PK_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custname = models.CharField(db_column='CUSTNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idcard_no = models.CharField(db_column='IDCARD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sex_val = models.CharField(db_column='SEX_VAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    edu_background = models.CharField(db_column='EDU_BACKGROUND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    edu_background_val = models.CharField(db_column='EDU_BACKGROUND_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='MARITAL_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    marital_status_val = models.CharField(db_column='MARITAL_STATUS_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rresidence_address = models.CharField(db_column='RRESIDENCE_ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rresidence_prov_name = models.CharField(db_column='RRESIDENCE_PROV_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rresidence_city_name = models.CharField(db_column='RRESIDENCE_CITY_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rresidence_area_name = models.CharField(db_column='RRESIDENCE_AREA_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rresidence_address_detail = models.CharField(db_column='RRESIDENCE_ADDRESS_DETAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rresidence_zip_code = models.CharField(db_column='RRESIDENCE_ZIP_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    come_here_date = models.CharField(db_column='COME_HERE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    raise_person = models.CharField(db_column='RAISE_PERSON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    child_number = models.CharField(db_column='CHILD_NUMBER', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_borrower_info'


class ZhbCdCarInfo(models.Model):
    car_pk_id = models.CharField(db_column='CAR_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loan_pk_id = models.CharField(db_column='LOAN_PK_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    car_hava = models.CharField(db_column='CAR_HAVA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    car_hava_val = models.CharField(db_column='CAR_HAVA_VAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price_car = models.CharField(db_column='PRICE_CAR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    car_age = models.CharField(db_column='CAR_AGE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loan_date = models.CharField(db_column='LOAN_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mortgage_monthly = models.CharField(db_column='MORTGAGE_MONTHLY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loan_ceiling = models.CharField(db_column='LOAN_CEILING', max_length=20, blank=True, null=True)  # Field name made lowercase.
    period_val = models.CharField(db_column='PERIOD_VAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    banlance_val = models.CharField(db_column='BANLANCE_VAL', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_car_info'


class ZhbCdCareerInfo(models.Model):
    rinfo_pk_id = models.CharField(db_column='RINFO_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loan_pk_id = models.CharField(db_column='LOAN_PK_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    is_private_owners = models.CharField(db_column='IS_PRIVATE_OWNERS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_private_owners_val = models.CharField(db_column='IS_PRIVATE_OWNERS_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    employees_num = models.CharField(db_column='EMPLOYEES_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    industry_in = models.CharField(db_column='INDUSTRY_IN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    industry_in_val = models.CharField(db_column='INDUSTRY_IN_VAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    founded_date = models.CharField(db_column='FOUNDED_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    full_work_name = models.CharField(db_column='FULL_WORK_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    company_kind = models.CharField(db_column='COMPANY_KIND', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_kind_val = models.CharField(db_column='COMPANY_KIND_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    work_department = models.CharField(db_column='WORK_DEPARTMENT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='POSITION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    position_val = models.CharField(db_column='POSITION_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    position_txt = models.CharField(db_column='POSITION_TXT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_prov_name = models.CharField(db_column='COMPANY_PROV_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    company_city_name = models.CharField(db_column='COMPANY_CITY_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    company_area_name = models.CharField(db_column='COMPANY_AREA_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salary_monthly = models.CharField(db_column='SALARY_MONTHLY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    othter_income_monthly = models.CharField(db_column='OTHTER_INCOME_MONTHLY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    start_work_time = models.CharField(db_column='START_WORK_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_size = models.CharField(db_column='COMPANY_SIZE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_size_val = models.CharField(db_column='COMPANY_SIZE_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    work_dept = models.CharField(db_column='WORK_DEPT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    social_security = models.CharField(db_column='SOCIAL_SECURITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    social_security_val = models.CharField(db_column='SOCIAL_SECURITY_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_career_info'


class ZhbCdCollection(models.Model):
    collection_id = models.CharField(db_column='COLLECTION_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contno = models.CharField(db_column='CONTNO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bal = models.DecimalField(db_column='BAL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overdays = models.CharField(db_column='OVERDAYS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prodid = models.CharField(db_column='PRODID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prodname = models.CharField(db_column='PRODNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sterm = models.CharField(db_column='STERM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    signtotalamt = models.DecimalField(db_column='SIGNTOTALAMT', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tcapi = models.DecimalField(db_column='TCAPI', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    begindate = models.CharField(db_column='BEGINDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scapi = models.DecimalField(db_column='SCAPI', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sinte = models.DecimalField(db_column='SINTE', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overbal = models.DecimalField(db_column='OVERBAL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overinte = models.DecimalField(db_column='OVERINTE', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    oversafine = models.DecimalField(db_column='OVERSAFINE', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    oversfoul = models.DecimalField(db_column='OVERSFOUL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    oversumbal = models.DecimalField(db_column='OVERSUMBAL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    realbal = models.DecimalField(db_column='REALBAL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    realdate = models.CharField(db_column='REALDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_id = models.CharField(db_column='STORE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    area_id = models.CharField(db_column='AREA_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    area_name = models.CharField(db_column='AREA_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_manager_id = models.CharField(db_column='CUST_MANAGER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_manager_name = models.CharField(db_column='CUST_MANAGER_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pos_type = models.CharField(db_column='POS_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pos_type_val = models.CharField(db_column='POS_TYPE_VAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    balancebal = models.DecimalField(db_column='BALANCEBAL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_collection'


class ZhbCdCreditEvaluateInfo(models.Model):
    cei_pk_id = models.CharField(db_column='CEI_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    card_account_number = models.CharField(db_column='CARD_ACCOUNT_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    no_cancel_card_account = models.CharField(db_column='NO_CANCEL_CARD_ACCOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    card_current_overdue_amount = models.CharField(db_column='CARD_CURRENT_OVERDUE_AMOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    card_overdue_months = models.CharField(db_column='CARD_OVERDUE_MONTHS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    card_overdue_number = models.CharField(db_column='CARD_OVERDUE_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    home_no_cancel_account = models.CharField(db_column='HOME_NO_CANCEL_ACCOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    home_current_overdue_amount = models.CharField(db_column='HOME_CURRENT_OVERDUE_AMOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    home_overdue_months = models.CharField(db_column='HOME_OVERDUE_MONTHS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    home_overdue_number = models.CharField(db_column='HOME_OVERDUE_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_no_cancel_account = models.CharField(db_column='OTHER_NO_CANCEL_ACCOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_monthly_repayment_amount = models.CharField(db_column='OTHER_MONTHLY_REPAYMENT_AMOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    loan_amount_three = models.CharField(db_column='LOAN_AMOUNT_THREE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_current_overdue_amount = models.CharField(db_column='OTHER_CURRENT_OVERDUE_AMOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_first_credit_year = models.CharField(db_column='OTHER_FIRST_CREDIT_YEAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_overdue_months = models.CharField(db_column='OTHER_OVERDUE_MONTHS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_overdue_number = models.CharField(db_column='OTHER_OVERDUE_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_1_months = models.CharField(db_column='LAST_1_MONTHS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_1_months_self = models.CharField(db_column='LAST_1_MONTHS_SELF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_3_months = models.CharField(db_column='LAST_3_MONTHS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_6_months = models.CharField(db_column='LAST_6_MONTHS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remainder = models.CharField(db_column='REMAINDER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contract_value = models.CharField(db_column='CONTRACT_VALUE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    outstanding_loan_amount = models.CharField(db_column='OUTSTANDING_LOAN_AMOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    creditc_total = models.CharField(db_column='CREDITC_TOTAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    creditc_max = models.CharField(db_column='CREDITC_MAX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    creditc_used = models.CharField(db_column='CREDITC_USED', max_length=20, blank=True, null=True)  # Field name made lowercase.
    first_card_year = models.CharField(db_column='FIRST_CARD_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mortgage_total = models.CharField(db_column='MORTGAGE_TOTAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mortgage_balance = models.CharField(db_column='MORTGAGE_BALANCE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    home_monthly_repayment_amount = models.CharField(db_column='HOME_MONTHLY_REPAYMENT_AMOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_credit_year = models.CharField(db_column='FIRST_CREDIT_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    a_other_loans_number = models.CharField(db_column='A_OTHER_LOANS_NUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_credit_evaluate_info'


class ZhbCdHoomsunRepayment(models.Model):
    repayment_id = models.CharField(db_column='REPAYMENT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sterm1 = models.CharField(db_column='STERM1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm2 = models.CharField(db_column='STERM2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm3 = models.CharField(db_column='STERM3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm4 = models.CharField(db_column='STERM4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm5 = models.CharField(db_column='STERM5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm6 = models.CharField(db_column='STERM6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm7 = models.CharField(db_column='STERM7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm8 = models.CharField(db_column='STERM8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm9 = models.CharField(db_column='STERM9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm10 = models.CharField(db_column='STERM10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm11 = models.CharField(db_column='STERM11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm12 = models.CharField(db_column='STERM12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm13 = models.CharField(db_column='STERM13', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm14 = models.CharField(db_column='STERM14', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm15 = models.CharField(db_column='STERM15', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm16 = models.CharField(db_column='STERM16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm17 = models.CharField(db_column='STERM17', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm18 = models.CharField(db_column='STERM18', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm19 = models.CharField(db_column='STERM19', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm20 = models.CharField(db_column='STERM20', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm21 = models.CharField(db_column='STERM21', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm22 = models.CharField(db_column='STERM22', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm23 = models.CharField(db_column='STERM23', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm24 = models.CharField(db_column='STERM24', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm25 = models.CharField(db_column='STERM25', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm26 = models.CharField(db_column='STERM26', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm27 = models.CharField(db_column='STERM27', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm28 = models.CharField(db_column='STERM28', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm29 = models.CharField(db_column='STERM29', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm30 = models.CharField(db_column='STERM30', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm31 = models.CharField(db_column='STERM31', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm32 = models.CharField(db_column='STERM32', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm33 = models.CharField(db_column='STERM33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm34 = models.CharField(db_column='STERM34', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm35 = models.CharField(db_column='STERM35', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sterm36 = models.CharField(db_column='STERM36', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_hoomsun_repayment'


class ZhbCdLoanCreditInfo(models.Model):
    lcinfo_pk_id = models.CharField(db_column='LCINFO_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apprvid = models.CharField(db_column='APPRVID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apprvname = models.CharField(db_column='APPRVNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finalapprvid = models.CharField(db_column='FINALAPPRVID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    finalapprvname = models.CharField(db_column='FINALAPPRVNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    trial_primary_opinion = models.CharField(db_column='TRIAL_PRIMARY_OPINION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trial_inner_opinion = models.TextField(db_column='TRIAL_INNER_OPINION', blank=True, null=True)  # Field name made lowercase.
    final_primary_opinion = models.CharField(db_column='FINAL_PRIMARY_OPINION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    apprvtime = models.CharField(db_column='APPRVTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apprvfinaltime = models.CharField(db_column='APPRVFINALTIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approv_amount = models.CharField(db_column='APPROV_AMOUNT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    final_approv_amount = models.CharField(db_column='FINAL_APPROV_AMOUNT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apptcapi = models.CharField(db_column='APPTCAPI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    final_approv_prodname = models.CharField(db_column='FINAL_APPROV_PRODNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    final_approv_period_val = models.CharField(db_column='FINAL_APPROV_PERIOD_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_return = models.CharField(db_column='IS_RETURN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_reconsider = models.CharField(db_column='IS_RECONSIDER', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_loan_credit_info'


class ZhbCdLoanDataEvaluate(models.Model):
    lde_pk_id = models.CharField(db_column='LDE_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    income = models.CharField(db_column='INCOME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    work_prov_valid = models.CharField(db_column='WORK_PROV_VALID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    work_prov_valid_val = models.CharField(db_column='WORK_PROV_VALID_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    work_prov_valid_txt = models.CharField(db_column='WORK_PROV_VALID_TXT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    has_business_net_info = models.CharField(db_column='HAS_BUSINESS_NET_INFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    has_business_net_info_val = models.CharField(db_column='HAS_BUSINESS_NET_INFO_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    has_business_net_info_txt = models.CharField(db_column='HAS_BUSINESS_NET_INFO_TXT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    address_prov_valid = models.CharField(db_column='ADDRESS_PROV_VALID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address_prov_valid_val = models.CharField(db_column='ADDRESS_PROV_VALID_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_prov_valid_txt = models.CharField(db_column='ADDRESS_PROV_VALID_TXT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    has_property = models.CharField(db_column='HAS_PROPERTY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    has_property_val = models.CharField(db_column='HAS_PROPERTY_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    verified_income = models.CharField(db_column='VERIFIED_INCOME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    verified_debet = models.CharField(db_column='VERIFIED_DEBET', max_length=20, blank=True, null=True)  # Field name made lowercase.
    theory_approv_amount = models.CharField(db_column='THEORY_APPROV_AMOUNT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    credit_debt_ratio = models.CharField(db_column='CREDIT_DEBT_RATIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loan_data_analy = models.CharField(db_column='LOAN_DATA_ANALY', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    trial_inner_opinion = models.TextField(db_column='TRIAL_INNER_OPINION', blank=True, null=True)  # Field name made lowercase.
    credit_info_evaluate = models.CharField(db_column='CREDIT_INFO_EVALUATE', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_loan_data_evaluate'


class ZhbCdLoanInfo(models.Model):
    loan_pk_id = models.CharField(db_column='LOAN_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operater_id = models.CharField(db_column='OPERATER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operater_name = models.CharField(db_column='OPERATER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    store_id = models.CharField(db_column='STORE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apply_date = models.CharField(db_column='APPLY_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apply_prodid = models.CharField(db_column='APPLY_PRODID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apply_prodname = models.CharField(db_column='APPLY_PRODNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    apply_amount = models.CharField(db_column='APPLY_AMOUNT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apply_time_limit = models.CharField(db_column='APPLY_TIME_LIMIT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    apply_time_limit_val = models.CharField(db_column='APPLY_TIME_LIMIT_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sales_person_id = models.CharField(db_column='SALES_PERSON_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sales_person_name = models.CharField(db_column='SALES_PERSON_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    team_manager_id = models.CharField(db_column='TEAM_MANAGER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    team_manager_name = models.CharField(db_column='TEAM_MANAGER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    urgency = models.CharField(db_column='URGENCY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    urgency_val = models.CharField(db_column='URGENCY_VAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_round_status = models.CharField(db_column='IS_ROUND_STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_round_status_val = models.CharField(db_column='IS_ROUND_STATUS_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_loan_info'


class ZhbCdLoanbal(models.Model):
    loanbal_id = models.CharField(db_column='LOANBAL_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    loanid = models.CharField(db_column='LOANID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contno = models.CharField(db_column='CONTNO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    custname = models.CharField(db_column='CUSTNAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    paperid = models.CharField(db_column='PAPERID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prodid = models.CharField(db_column='PRODID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    prodname = models.CharField(db_column='PRODNAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tcapi = models.DecimalField(db_column='TCAPI', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    signtotalamt = models.DecimalField(db_column='SIGNTOTALAMT', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tterm = models.CharField(db_column='TTERM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    begindate = models.CharField(db_column='BEGINDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='ENDDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    firstretudate = models.CharField(db_column='FIRSTRETUDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    signdate = models.CharField(db_column='SIGNDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    store_id = models.CharField(db_column='STORE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operid = models.CharField(db_column='OPERID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opername = models.CharField(db_column='OPERNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pos_type = models.CharField(db_column='POS_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pos_type_val = models.CharField(db_column='POS_TYPE_VAL', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_loanbal'


class ZhbCdPropertyInfo(models.Model):
    pinfo_pk_id = models.CharField(db_column='PINFO_PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    loan_pk_id = models.CharField(db_column='LOAN_PK_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    house_prov_name = models.CharField(db_column='HOUSE_PROV_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    house_city_name = models.CharField(db_column='HOUSE_CITY_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    house_area_name = models.CharField(db_column='HOUSE_AREA_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_house_date = models.CharField(db_column='START_HOUSE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rent_monthly_pay = models.CharField(db_column='RENT_MONTHLY_PAY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    property_type = models.CharField(db_column='PROPERTY_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    property_type_val = models.CharField(db_column='PROPERTY_TYPE_VAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mortgage_monthly_pay = models.CharField(db_column='MORTGAGE_MONTHLY_PAY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    buy_time = models.CharField(db_column='BUY_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    buy_price = models.CharField(db_column='BUY_PRICE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gfa = models.CharField(db_column='GFA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_home_address = models.CharField(db_column='IS_HOME_ADDRESS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_home_address_val = models.CharField(db_column='IS_HOME_ADDRESS_VAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    property_prov_name = models.CharField(db_column='PROPERTY_PROV_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    property_city_name = models.CharField(db_column='PROPERTY_CITY_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    property_area_name = models.CharField(db_column='PROPERTY_AREA_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loan_life = models.CharField(db_column='LOAN_LIFE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loans = models.CharField(db_column='LOANS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    credit_period = models.CharField(db_column='CREDIT_PERIOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    live_conditions = models.CharField(db_column='LIVE_CONDITIONS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    live_conditions_val = models.CharField(db_column='LIVE_CONDITIONS_VAL', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zhb_cd_property_info'


class ZkbcCdExcelexpSetting(models.Model):
    pk_id = models.CharField(db_column='PK_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    query_key = models.CharField(db_column='QUERY_KEY', max_length=64, blank=True, null=True)  # Field name made lowercase.
    headers = models.CharField(db_column='HEADERS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    value_columns = models.CharField(db_column='VALUE_COLUMNS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pagination_number = models.CharField(db_column='PAGINATION_NUMBER', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zkbc_cd_excelexp_setting'
