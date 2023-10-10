# example/urls.py
from django.urls import path
from MyApp.views import compute
from MyApp.views import index


urlpatterns = [
    path('', index),
    path('compute_graph/', compute_graph, name='compute_graph'),
    path('compute_impact/', compute_impact, name='compute_impact'),
]