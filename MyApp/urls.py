# example/urls.py
from django.urls import path

from MyApp.views import index


urlpatterns = [
    path('', index),
    path('button_pressed/', views.button_pressed, name='button_pressed'),
]