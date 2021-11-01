from django.contrib.auth.models import User
from .models import Profile
from django import forms


class UserForm(forms.ModelForm):
      class Meta:
            model = User
            fields = ['first_name', 'last_name', 'username', 'email']

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({"class":"form-control register", "placeholder":"first_name"})
            self.fields['last_name'].widget.attrs.update({"class":"form-control register", "placeholder":"last_name"})
            self.fields['username'].widget.attrs.update({"class":"form-control register", "placeholder":"username"})
            self.fields['email'].widget.attrs.update({"class":"form-control register", "placeholder":"email"})


class ProfileForm(forms.ModelForm):
      
      class Meta:
            model = Profile
            fields = '__all__'

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["address"].widget.attrs.update({"class":"form-control register", "placeholder":"Address"})
            self.fields["city"].widget.attrs.update({"class":"form-control register", "placeholder":"City"})
            self.fields["state"].widget.attrs.update({"class":"form-control register", "placeholder":"State"})
            self.fields["country"].widget.attrs.update({"class":"form-control register", "placeholder":"Country"})
            self.fields["zipcode"].widget.attrs.update({"class":"form-control register", "placeholder":"Zipcode"})
            self.fields["phone_no"].widget.attrs.update({"class":"form-control register", "placeholder":"Phone Number"})
            self.fields["profile_picture"].widget.attrs.update({"class":"form-control"})