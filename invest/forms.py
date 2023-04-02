from django import forms 
from .models import *


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ("asset","image","name")
        

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ("amount","wallet","name")   
        
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("name","email","phone","body")                