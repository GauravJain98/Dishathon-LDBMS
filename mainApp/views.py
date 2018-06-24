from django.shortcuts import render,redirect
from requests import get
from .models import *
from django.utils import timezone

def get_info(ip):
    url = "http://api.ipstack.com/"+ip+"?access_key=8d753f2f0041e95c7a3a5ad6de000c2f"

    data = get(url).json()
    return (data['zip'],data['city'])

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def addLead(request):
    if request.method == 'POST':
        name = request.POST['name']    
        phone = request.POST['phone']    
        ip = get_client_ip(request)
        zip_code , city = get_info(ip)
        lead = Lead.objects.create(name= name,phone = phone)
        lead.save()
    return render(request,'addLead.html')

def change(request,id):
    lead = Lead.objects.get(id=id)
    if int(lead.price) < int(request.POST['bid']):
        lead.price = request.POST['bid']
        lead.choose = Distributor.objects.get(user = request.user)
    lead.save()
    return redirect('/distributor/')

def update(request,id):
    lead = Lead.objects.get(id=id)
    lead.name = request.POST['name'] 
    if 'description' in request.POST:
        lead.description = request.POST['description']
    if 'address' in request.POST:
        lead.address = request.POST['address']
    lead.save()
    return redirect('/dLead')

def lead(request,id):
    if request.method == 'POST':
        lead.acquired = request.POST['acquired'] == 'on'
        lead.total = lead.total + 1
        lead.save()
        return redirect('/lead/'+str(id))
    return render(request,'lead.html')

def distributor(request):
    if 'city' in request.GET:
        leads = Lead.objects.filter(city__contains = request.GET['city']).extra(order_by = ['price'])
    else:
        leads = Lead.objects.extra(order_by = ['price'])
    for lead in leads:
        lead.timeleft = (lead.time*60)- (timezone.now() - lead.date).total_seconds()
    return render(request,'distribution.html',{'leads':leads})

def dLead(request):
    leads = Lead.objects.filter(choose__user = request.user)
    return render(request,'acqlead.html',{'leads':leads})
    