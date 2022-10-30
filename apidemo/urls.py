from django.contrib import admin
from django.urls import path 

from .views import firstview

urlpatterns = [
    path('',firstview.as_view())
]