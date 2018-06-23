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

class Lead(models.Model):
    name = models.CharField(max_length=30,blank=False)
    phone = models.CharField(max_length=10,blank=False)
    ip = models.CharField(max_length=15,blank=False)
    city = models.CharField(max_length=30,blank=False)
    choose = models.ForeignKey(
        Distributor,
        null = True,
        on_delete=models.CASCADE,
    )
    near = models.ManyToManyField(
        Distributor,
        related_name = 'closests',
    )
