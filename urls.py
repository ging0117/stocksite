"""stocksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from stock import views
from django.contrib.auth.decorators import login_required
from stock.views import StockCreate

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^accounts/login/',auth_views.login),
    url(r'^logout/$',auth_views.logout, {'next_page':'home'}),
    url(r'^add_stock/',login_required(StockCreate.as_view(success_url="/"))),
    url(r'^stocks/',views.stockView,name='StockList'),
]
