from django.db import models
from django.contrib.auth.models import User

class Distributor(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name = 'User',
        null = False,
        unique = True
    )
    zipcode = models.CharField(max_length=6,null=False)
    city = models.CharField(max_length=30,null=False)
    phone = models.CharField(max_length=10,blank=False)
    aquired = models.FloatField (default = 0)
    total = models.IntegerField (default = 0)

class Lead(models.Model):
    name = models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=10)
    timeleft = models.DateTimeField(blank=True)
    zipcode = models.CharField(max_length=6,blank=True)
    time = models.IntegerField(default=50)
    city = models.CharField(max_length=30,blank=True)
    price = models.IntegerField(default = 50,blank=True)
    date = models.DateTimeField(auto_now_add =True,blank=True)
    description = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=200,blank=True)
    choose = models.ForeignKey(
        Distributor,
        null = True,
        on_delete=models.CASCADE,
    )
