
from django.shortcuts import redirect
from django.contrib import messages



class ValidatePaymentDetails():
      def __init__(self, card_number, cvv, exp) :
          self.card_number = card_number
          self.cvv = cvv
          self.exp = exp
      
      def validate_details(self, request):
            if type(self.card_number) != int:
                  messages.warning(request, "card input not a number")
                  return redirect("billing-view")

            elif len(self.card_number) > 16 or len(self.card_number) < 16:
                  messages.warning(request, " this should contain a 16 digit number")
                  return redirect("billing-view")

            elif (self.card_number == ""):
                  messages.warning(request, "card number field cannot be empty")
                  return redirect("billing-view")

            elif type(self.cvv) != int:
                  messages.warning(request, "cvv input not a number")
                  return redirect("billing-view")

            elif len(self.cvv) > 3 or len(self.cvv) < 3:
                  messages.warning(request, "this should contain a 3 digit number")
                  return redirect("billing-view")

            elif (self.cvv == ""):
                  messages.warning(request, "cvv number field cannot be empty")
                  return redirect("billing-view")

            elif len(self.exp) > 5 or len(self.exp) < 5:
                  messages.warning(request, "this should follow month/year format")
                  return redirect("billing-view")

            elif self.exp == "":
                  messages.warning(request, "exp field cannot be empty")
                  return redirect("billing-view")