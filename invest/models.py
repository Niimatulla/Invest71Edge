from django.db import models
from users.models import CustomUser


# Create your models here.

asset = (
     ('Silver','Silver'),
    ('Gold','Gold'),
    ('Diamond','Diamond'),
    ('Mercury','Mercury'),
)

class Asset(models.Model):
    name = models.CharField(max_length=50, choices=asset, null=True, verbose_name="Asset name")
    body = models.TextField(verbose_name="Asset Descriptions")
    image = models.ImageField(upload_to="Asset images", verbose_name="Assert Image")
    price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
class Buy(models.Model):
    asset = models.CharField(max_length=50, choices=asset) 
    name = models.CharField(max_length=50, verbose_name="Full name")    
    image = models.ImageField(upload_to="Asset Receipt", verbose_name="payment prove")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} -- {self.asset}"
    

class Withdraw(models.Model):
    amount = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50, verbose_name="Full name") 
    wallet = models.CharField(max_length=50, verbose_name="Customer wallet address Usdt(Trc20)")
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.name} -- ${self.amount}" 
    
      
class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50, verbose_name="Full name")
    body = models.TextField(verbose_name="Message")  
    phone = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} -- Messages"    