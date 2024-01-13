from django.urls import path , include
from .views import (LoginView , UserView )
from rest_framework_simplejwt.views import TokenRefreshView
app_name = 'users'

urlpatterns = [
    path("auth/login/", LoginView.as_view(), 
         name="login"),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]