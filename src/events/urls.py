"""myuniverse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='/'),
    path('info/', views.info, name='info'),
    path('concert/', views.concert, name = 'concert'),
    path('menuticket/',views.menuticket, name='menuticket'),
    path('conall/<code>',views.conall,name='conall'),
    path('condate/<code>',views.condate, name='condate'),
    path('conart/',views.conart, name = 'conart'),
    path('conrank/',views.conrank, name = 'conrank'),
    path('fuel/',views.fuelcharge, name = 'fuelcharge'),
    path('search',views.searchcon, name ='search'),
    path('detailedsearch',views.detailedsearch, name ='detailedsearch'),
    # 사용자별로 수정필요
    path('mypage/',views.mypage, name = 'mypage'),
    # 포스터별로 수정 필요
    # path('posdetail/<code>/', views.get_posdetail, name = 'get_posdetail'),
    # path('ticketing/<code>/', views.ticketing, name = 'ticketing'),

    path('posdetail/<code>/', views.posdetail, name = 'posdetail'),
    path('ticketing/<code>/', views.ticketing, name = 'ticketing'),
    path('artpop/<code>/',views.artpop, name = 'artpop'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
