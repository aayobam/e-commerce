from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
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
def updateprofile(request):
    template_name = "accounts/user-profile.html"
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    address=request.POST.get('address')
    city=request.POST.get('city')
    state=request.POST.get('state')
    country=request.POST.get('country')
    phone_no=request.POST.get('phone_no')
    zipcode=request.POST.get('zipcode')
    profile_image=request.POST.get('profile_image')
    

    if request.method == 'POST':
        u1=User.objects.get(username=request.user)
        u1.first_name=first_name
        u1.last_name=last_name
        u1.username=username
        u1.email=email
        u1.save()
        print("user updated")
        user_profile = Profile.objects.get(request.user, instance=u1)
        user_profile.address=address
        user_profile.city=city
        user_profile.state=state
        user_profile.phone_no=phone_no
        user_profile.zipcode=zipcode
        user_profile.country=country
        user_profile.profile_picture=profile_image
        if user_profile:
            user_profile.save()
            messages.success(request,f'Your Profile has been updated!')
            return redirect('product_list')
        else:
            messages.success(request, f'update your profile')
            return redirect("accounts:user-profile")
    else:
        context = {"profile_profile":profile_image}
    return render(request, template_name, context)
