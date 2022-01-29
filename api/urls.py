from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('correlation/', views.correlation_view, name='correlation-view'),
    path('calculate/', views.calculate_view, name='calculate-view'),
    path('users/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
