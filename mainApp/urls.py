from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^addLead/', views.addLead,name='addLead'),
    url(r'^distributor/', views.distributor,name='distributor'),
]