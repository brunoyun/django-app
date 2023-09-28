# example/urls.py
from django.urls import path

from MyApp.views import index


urlpatterns = [
    path('', index),
]