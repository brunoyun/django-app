# example/urls.py
from django.urls import path
from MyApp.views import compute
from MyApp.views import index


urlpatterns = [
    path('', index),
    path('compute/', views.compute, name='compute'),
]