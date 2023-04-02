from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username","email","first_name","last_name","phone","address","wallet") 


class UserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username","email","first_name","last_name","phone","address","wallet")