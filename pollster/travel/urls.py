from django.contrib import admin
from django.urls import path
from travel import views

urlpatterns = [
    path("",views.home,name='travel')
]