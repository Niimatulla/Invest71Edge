from django.urls import path  
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('buy/', views.buy, name="buy"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('withdraw/', views.withdraw, name="withdraw"),
    path('adm1/', views.adm1, name="adm1"),
    path('adm2/', views.adm2, name="adm2"),
    path('message/', views.message, name="message"),
    path('messages/', views.msm, name="msm"),
    
]
