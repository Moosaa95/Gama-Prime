from django.contrib import admin
from .models import User, Profile
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_admin')
    # list_filter = ('is_admin',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ('user', 'profile_pic', 'bio', 'website', 'phone_number', 'created_at', 'updated_at')
    # list_filter = ('is_admin',)
    pass