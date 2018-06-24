from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('change/<int:id>/', views.change),
    path('lead/<int:id>/', views.lead),
    path('update/<int:id>/', views.update),
    url(r'^addLead/', views.addLead,name='addLead'),
    url(r'^dLead/', views.dLead,name='dLead'),
    url(r'^distributor/', views.distributor,name='distributor'),
]