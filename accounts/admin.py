from django.contrib import admin
from .models import Profile




@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'address', 'zipcode', 'city', 'state', 'country', 'phone_no', 'profile_picture', 'created_at', 'updated_at')
    list_filter = ('phone_no',)
