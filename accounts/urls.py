from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "accounts"

urlpatterns = [
    path('register/', user_registration, name="user-registration"),
    path('login/', user_login, name="user-login"),
    path("logout/", logout, name="logout"),
    path('updateprofile/<int:pk>/', updateprofile, name="user-profile"),



    # Password Reset
    path(
        'reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            subject_template_name='accounts/password_reset_subject.txt',
            email_template_name='accounts/password_reset_email.html',
            success_url='done'
        ),
        name='password_reset'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url='/accounts/reset_confirm/complete/'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset_confirm/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
