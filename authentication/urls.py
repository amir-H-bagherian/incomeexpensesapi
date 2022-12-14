from django.urls import path
from .views import RegisterView, VerifyEmail, SetNewPasswordAPIView, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail
## Erase this if faced an error
from rest_framework_simplejwt.views import (TokenRefreshView, )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    # Erase this if faced an error
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]