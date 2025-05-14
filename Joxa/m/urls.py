from django.contrib import admin
from django.urls import path
from .views import say_joxa, say_hello

urlpatterns = [
    path('Joxa/', say_joxa),
    path('hello/', say_hello),
]
