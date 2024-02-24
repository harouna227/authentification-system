from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import *


urlpatterns = [
    path("", profile , name='profile'),
    path("register/", register , name='register'),
    
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout/", logout_user, name='logout_user'),
    # path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("password-change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("password-reset/compete/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]