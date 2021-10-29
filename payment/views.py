from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cartapp.cart import Cart
from accounts.models import Profile
from django.contrib import messages
from orders.models import *
from .models import Card
from e_commerce.settings import DEFAULT_FROM_EMAIL
from accounts.mail_notifocations import MailNotificationForOrders
from .validate_card_details import ValidatePaymentDetails





#Billing details view
@login_required(login_url="accounts:user-login")
def billing_view(request):
      profile = Profile.objects.get(user=request.user)
      if (profile.address=="" and profile.zipcode=="" and profile.city=="" and profile.state=="" and profile.country==""):
            messages.info(request, "you have to update your profile to place your orders")
            return redirect("accounts:user-profile")
      template_name = "payment/payment.html"
      cart = Cart(request)
      total_price = str(cart.get_total_price())
      total = total_price
      context = {"total":total, "profile":profile}
      return render(request, template_name, context)


#card details form
def card_form_view(request):
      profile = Profile.objects.get(user=request.user)
      template_name = "payment/payment.html"
      cart = Cart(request)
      total = cart.get_total_price()
      if request.method == 'POST':
            card = request.POST.get("card_number")
            cvv = request.POST.get("cvv")
            exp = request.POST.get("exp")
            card_details = Card.objects.create(user=profile.user, card_number = card, cvv=cvv, exp=exp)
            # validate_payment = ValidatePaymentDetails(card_number=card_details.card_number, cvv=card_details.cvv, exp=card_details.exp)
            # validate_payment.validate_details(request)
            
            order = Order.objects.create(
                  user = profile.user,
                  first_name = profile.user.first_name,
                  last_name = profile.user.last_name,
                  email = profile.user.email,
                  address =  profile.address,
                  zipcode = profile.zipcode,
                  total_amount = total,
                  payment_status = True,
            )
            order_id=order.pk
            for item in cart:
                  OrderItem.objects.create(order_id=order_id, product=item["product"],price=item["price"], quantity=item["qty"])
                  messages.success(request, "order successful")

                  # mail config
                  recipient_email = profile.user.email
                  sender_email = DEFAULT_FROM_EMAIL
                  mail_subject = "order successfully placed" 
                  message_body = f"hello {profile.user.first_name} {profile.user.last_name} your order was sucessfully place"   
                  send_mail_for_orders = MailNotificationForOrders(
                        recipient_email=recipient_email, 
                        sender_email=sender_email, 
                        mail_subject=mail_subject, 
                        message_body=message_body
                  )
                  # send_mail_for_orders.mail_new_customer()
                  # send_mail_for_orders.mail_admin()
                  return redirect("order-success")
            else:
                  messages.error(request, "order not successful")
                  return redirect("billing-view")
      else:
            context = {"total":total}
      return render(request, template_name, context)


def order_status(request):
      template_name = "payment/orderplace.html"
      return render(request, template_name)
