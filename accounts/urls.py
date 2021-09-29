from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', user_account, name="user-account"),
    path('register/', user_registration, name="user-registration"),
    path('login/', user_login, name="user-login"),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password-reset/password_reset.html',
            subject_template_name='password-reset/password_reset_subject.txt',
            email_template_name='password-reset/password_reset_email.html',
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password-reset/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password-reset/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password-reset/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),    
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
]
