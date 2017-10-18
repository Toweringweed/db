from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import contract_t, contract, orders
from datetime import datetime
from django.http import JsonResponse
import json

def default(request):
    return render(request, 'default.html')

def test(request):
    return render(request, 'test.html')

def ajax_html(request):
    with open(r'E:\hoomsun_data\db\datago\json\xian.json', 'r', encoding='utf-8') as ff:
        ll = json.load(ff)

    return HttpResponse(ll)

def ajax_dict(request):
    with open(r'E:\hoomsun_data\db\datago\json\product.json', 'r', encoding='utf-8') as ff:
        ll = json.load(ff)

    return JsonResponse(ll, safe=False)

def ajax_map(request):
    with open(r'E:\hoomsun_data\db\datago\json\city_contract.json', 'r', encoding='utf-8') as ff:
        data = json.load(ff)
    return JsonResponse(data, safe=False)

def ajax_contract_today(request):
    with open(r'E:\hoomsun_data\db\datago\json\contract_today.json', 'r', encoding='utf-8') as ff:
        data = json.load(ff)
    return JsonResponse(data, safe=False)

