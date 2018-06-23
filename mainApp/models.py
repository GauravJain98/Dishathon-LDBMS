from django.db import models

class Distributor(models.Model):
    user = models.OnetoOne(
        User,
        on_delete=models.CASCADE,
        verbose_name = 'User',
        null = False,
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
    )
    near = models.ManytoMany(
        Distributor,
        related_name = 'closests',
    )
