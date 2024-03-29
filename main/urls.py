﻿from django.urls import path, include

from main.apps import MainConfig
from main.views import index, contacts, category_main

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/serv/', category_main, name='category_main'),
    path('', include('django.contrib.auth.urls')), ]
