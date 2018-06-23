from django.shortcuts import render
from requests import get
from .models import *

def get_info(ip):
    url = "http://api.ipstack.com/"+ip+"?access_key=8d753f2f0041e95c7a3a5ad6de000c2f"

    data = requests.get(url).json()
    return (data['zip'],data['city'])

def addLead(requests):
    if request.method == 'POST':
        name = request.POST['name']    
        phone = request.POST['phone']    
        ip = request.POST['ip']    
        zip_code , city = get_info(ip)
        distributors = list(Distributor.objects.filter(city = city))
        lead = Lead(name= name,zip_code = zip_code,ip = ip,phone = phone)
        if len(distributor)>0:
            for distributor in distributors:
                lead.near.add(distributor)
            lead.save()
            return render(request,'addLead.html')
        else:
            return show(request,'No distributor in your city')
    else:
        return render(request,'addLead.html')

def distributor(requests):
    leads = list(Lead.objects.filter(near__user = request.user))
    if request.method == 'POST':
        lead = request.POST['lead']
        lead = Lead.objects.get(id = lead)
        lead.closest = Distributor.objects.get(user = request.user)
        lead.save() 
    return render(request,'distributor.html',{'leads':leads})
    