from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:    
        form = UserForm()
    
    context = {
        "form":form,
    }    
    
    return render(request, "registration/signup.html", context)