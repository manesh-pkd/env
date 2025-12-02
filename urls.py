from django.urls import path
from django.contrib import admin
from . import views

app_name = 'customer'

urlpatterns = [
     path('', views.home, name='home'),
    # path('', views.home, name='home'),
    # path('sighnup/', views.sighnup, name='sighnup'), 
    # path('login/', views.login, name='login'),
    path('sighnup/', views.sighnup, name='sighnup'),
    path('login/', views.login, name='login'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('csr/', views.csr, name='csr'),
    path('sustain/', views.sustain, name='sustain'),
    path('book/', views.book_gas, name='book_gas'),
]