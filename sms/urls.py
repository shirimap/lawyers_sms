from django.contrib import admin
from .views import *
from django.urls import path
app_name = 'sms'
urlpatterns = [
    path('demo', AlertUser)
]