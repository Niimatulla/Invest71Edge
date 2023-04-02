from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import CustomUser
from django.contrib.auth.models import User


class UserAdmin(UserAdmin):
    add_form = UserForm
    form = UserChange
    list_display = ['email', 'username', 'address','phone','first_name','last_name']
    model = CustomUser
    
    
admin.site.register(CustomUser)
admin.site.register(User, UserAdmin)
