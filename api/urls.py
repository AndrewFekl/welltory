from django.urls import path
from . import views



urlpatterns = [
    path('correlation/', views.correlation_view, name='correlation-view'),
    path('calculate/', views.calculate_view, name='calculate-view'),
]
