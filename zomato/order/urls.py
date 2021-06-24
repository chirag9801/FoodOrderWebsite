from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('add',views.add,name="add"),
    path('index',views.index,name="index"),
    path('useraccount',views.useraccount,name="useraccount")
]
