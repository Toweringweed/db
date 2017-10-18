"""db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from visual import views as visual_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', visual_view.default),
    url(r'^ajax_time/$', visual_view.ajax_time),
    url(r'^test/$', visual_view.test),
    url(r'^ajax_contract_money/$', visual_view.ajax_contract_money),
    url(r'^ajax_city/$', visual_view.ajax_city),
    url(r'^ajax_map/$', visual_view.ajax_map),
    url(r'^ajax_hp/$', visual_view.ajax_hp),
    url(r'^ajax_hp2/$', visual_view.ajax_hp2),
    url(r'^ajax_hp3/$', visual_view.ajax_hp3),
    url(r'^ajax_contract_today/$', visual_view.ajax_contract_today)

]

