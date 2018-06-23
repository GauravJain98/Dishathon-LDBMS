from django.shortcuts import render
from requests import get
from .models import *

def get_info(ip):
    url = "http://api.ipstack.com/"+ip+"?access_key=8d753f2f0041e95c7a3a5ad6de000c2f"

    data = requests.get(url).json()
    return (data['zip'],data['city'])



def addLead(request):
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

def distributor(request):
    if request.GET['city']:
        leads = Lead.objects.filter(city__contains = request.GET['city']).extra(order_by = ['prize'])
    if request.GET['ip']:
        leads = Lead.objects.filter(city__contains = request.GET['ip']).extra(order_by = ['prize'])
    else:
        leads = Lead.objects.extra(order_by = ['prize'])
    return render(request,'distribution.html',{'leads':leads})
    