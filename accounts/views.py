from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib import auth, messages
from .mail_notifocations import MailNotificationForRegisteration
from e_commerce.settings import DEFAULT_FROM_EMAIL
from .decorators import *
from django.contrib.auth.decorators import login_required
import time


# create user registration view
@authenticated_user
def user_registration(request):
    template_name = "accounts/register.html"
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect("accounts:user-registration")

                elif User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                    return redirect("accounts:user-registration")

                else:
                    user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password1)
                    user.save()
                    Profile.objects.get_or_create(user=user)
                    messages.success(request, f"account for {user.email} successfully created")

                    # initialize static data for mail notification
                    message_body = f"<h1>Hello {user.email}, your registration on bayshop is successful</h1>",
                    mail_subject = f"<h1>Registeration Successful</h1>"
                    sender_email = DEFAULT_FROM_EMAIL
                    recipient_email = user.email

                    send_notification = MailNotificationForRegisteration(recipient_email, sender_email, mail_subject, message_body)

                    # send_notification.mail_new_customer()
                    # send_notification.mail_admin()

                    # # send mail to admin(s)
                    # send_notification.mail_admin()
                    time.sleep(2)
                    return redirect("accounts:user-login")
        except User.DoesNotExist:
            messages.error(request, "Password don't match!")
            return redirect("accounts:user-registration")
    else:
        return render(request, template_name)


# create user view login
@authenticated_user
def user_login(request):
    template_name = "accounts/log-in.html"
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                messages.info(request, f'You are logged in as {username}')
                return redirect(request.POST.get('next'))
            else:
                return redirect("product_list") 
        else:
            messages.error(request, f'Invalid username or password')
            return redirect("accounts:user-login")
    else:
        return render(request, template_name, context={})


def logout(request):
    auth.logout(request)
    return redirect("product_list")


@login_required
def updateprofile(request, pk):
    template_name = "accounts/user-profile.html"
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"your profile was successfully updated")
            return redirect("accounts:user-profile", pk)
    else:
        u_form = UserForm(instance=user)
        p_form = ProfileForm(instance=profile)
    context = {"u_form":u_form, "p_form":p_form, "profile":profile}
    return render(request, template_name, context)


    
        