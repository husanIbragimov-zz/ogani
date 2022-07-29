from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('register/', views.AccountRegisterView.as_view()),
    path('verify-email/', views.EmailVerificationView.as_view(), name='verify-email'),
    path('login/', views.LoginView.as_view()),
    path('reset-password/', views.ResetPasswordView.as_view()),
    path('set-password-confirm/<str:uidb64>/<str:token>/', views.SetPasswordConfirmView.as_view()),
    path('set-password-completed/', views.SetNewPasswordCompletedView.as_view()),
    path('change-password/<int:pk>/', views.ChangePasswordCompletedView.as_view()),
    path('profile/<str:email>/', views.MyAccountAPIView.as_view())
]
