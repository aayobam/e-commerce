from django.db import models
from django.contrib.auth.models import User





class Card(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      card_number = models.CharField(max_length=16, blank=True, help_text="16 digit number")
      cvv = models.CharField(max_length=3, blank=True, help_text="3 digit number at the back of your card")
      exp = models.CharField(max_length=5, help_text="Expiry date of card")

      def __str__(self):
            return self.user.username