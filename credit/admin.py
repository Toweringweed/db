from django.contrib import admin
from django.forms import ModelForm, TextInput
from .models import basic, card, loan, chaxun1, chaxun2, summary, ggjl


class cardInline(admin.TabularInline):
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 30
        return max_num
    model = card


class loanInline(admin.TabularInline):
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 30
        return max_num
    model = loan

class ggjlInline(admin.TabularInline):
    model = ggjl
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num

class chaxun1Inline(admin.TabularInline):
    model = chaxun1
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 50
        return max_num

class chaxun2Inline(admin.TabularInline):
    model = chaxun2
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 50
        return max_num

class summaryInline(admin.StackedInline):
    fields = (('card_account', 'housing_loan_account', 'other_loan_account'),
              ('card_notsettled', 'housing_loan_notsettled', 'other_loan_notsettled'),
              ('card_overdue', 'housing_loan_overdue', 'other_loan_overdue'),
              ('card_90overdue', 'housing_loan_90overdue', 'other_loan_90overdue'),
              ('card_guaranty', 'housing_loan_guaranty', 'other_loan_guaranty')
              )
    class FlatPageAdmin(admin.ModelAdmin):
        fields = (('card_account', 'housing_loan_account', 'other_loan_account'),
                  ('card_notsettled', 'housing_loan_notsettled', 'other_loan_notsettled'),
                  ('card_overdue', 'housing_loan_overdue', 'other_loan_overdue'),
                  ('card_90overdue', 'housing_loan_90overdue', 'other_loan_90overdue'),
                  ('card_guaranty', 'housing_loan_guaranty', 'other_loan_guaranty')
                  )
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 1
        return max_num
    model = summary

class basicAdmin(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')
    list_display = ('order_id', 'name', 'IDcard', 'type', 'kongbai', 'luruyuan', 'luru')
    search_fields = ['order_id', 'name']

    list_editable = ['luru']
    fields = (('order_id', 'name', 'IDcard', 'type', 'kongbai'),

              )
    # readonly_fields = ['luruyuan']

    ordering = ['luru']

    def save_model(self, request, obj, form, change):

        if getattr(obj, 'luruyuan', None) == '':
            obj.luruyuan = str(request.user)
        obj.last_modified_by = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(basicAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(luruyuan=request.user)



    save_on_top = True

    list_per_page = 10
    inlines = [
        summaryInline, cardInline, loanInline, ggjlInline, chaxun1Inline, chaxun2Inline
    ]

    class Media:
        css = {"all": ("/static/css/my_style3.css",)}

admin.site.register(basic, basicAdmin)
admin.site.site_header = '红上征信录入'
admin.site.site_title = '红上征信录入'






