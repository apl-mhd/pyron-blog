from .import views
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.UserCreateAPIView.as_view(), name='api_register'),
]
