from django.urls import path
from user.api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('reset-password/', views.reset_password_view, name='change_password'),
    path('verify-email/', views.verify_email_view, name='verify_email'),
    path('resend-verification-email/', views.resend_verification_email_view, name='resend_verification_email'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]