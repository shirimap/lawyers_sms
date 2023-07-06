from django.contrib import admin
from .views import *
from django.urls import path
app_name = 'messages'
urlpatterns = [
    path('demo', AlertUser)
]