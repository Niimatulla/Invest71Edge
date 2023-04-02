from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from users.models import CustomUser
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    asset = Asset.objects.all()
    hmm = Withdraw.objects.count()
    hmm1 = Buy.objects.count()
    count = CustomUser.objects.count()
    
   
    context = {
        'asset':asset,
        "hmm":hmm,
        "hmm1":hmm1,
        "count":count,
    }
    return render(request, "pages/home.html", context)

@login_required
def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratualtion cheack your homepage in the next 40 min")
            return redirect("/")
        
        
        
        
    else:
        form = BuyForm()
    
    context = {
        "form":form
    }        
    return render(request, "pages/buy.html", context)


@login_required
def dashbord(request):
    now = datetime.datetime.now()
    p1 = 50
    p2 = 100
    p3 = 200
    p4 = 500
    
    w1 = p1 + 2.5
    w2 =  + 5
    w3 = p3 + 10 
    w4 = p4 + 25
    
    
    if w1 == now + datetime.timedelta(days=1):
        w1
    elif w2 == now + datetime.timedelta(days=1):
        w2
    elif w3 == now + datetime.timedelta(days=1):
        w3   
    elif w4 == now + datetime.timedelta(days=1):
        w4   
        
    else:
        0     
    
#    if  datetime.datetime.hour == 24:
#         w2 = p2 + 5 
    
    
    # if now.hour == 24:
    #     w1 = p1 + 2.5
 
    # if now.hour == 24:
    #     w2 = p2 + 5 
    # else:
    #     w2
    # if now.hour == 24:
    #     w3 = p3 + 10 
    # else:
    #     w3
    # if now.hour == 24:
    #     w4 = p4 + 25  
    # else:
    #     w4
   
                            

    context = {
        'p1':p1,
        'p2':p2,
        'p3':p3,
        'p4':p4,
        # 'w1':w1,
        'w2':w2,
        # 'w3':w3,
        # 'w4':w4,
    }
    return render(request, "pages/dashbord.html", context)


@login_required
def withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WithdrawForm()
    
    context = {
        'form':form
    }   
    
    return render(request, "pages/withdraw.html", context)  



@login_required
def adm1(request):
   form = Withdraw.objects.all()
#    name = CustomUser.first_name
#    wal = CustomUser.wallet
   context = {
        'form':form,
        # 'name':name,
        # 'wal':wal
    }   
    
   return render(request, "pages/adm1.html", context)     

@login_required
def adm2(request):
    form = Buy.objects.all()
    context = {
        'form':form
    }   
    return render(request, "pages/adm2.html", context)   

@login_required
def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    else:    
        form = MessageForm()
    
    context = {
        "form":form,
    }    
    
    return render(request, "registration/message.html", context)


@login_required
def msm(request):
    form = Message.objects.all()
    context = {
        "form":form,
    }    
    
    return render(request, "registration/msm.html", context)