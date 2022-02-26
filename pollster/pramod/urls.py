from django.contrib import admin
from django.urls import path
from pramod import views

urlpatterns = [
    path("",views.about,name='home'),
    path("store",views.add,name='add'),
    path("search",views.search,name='search')
]