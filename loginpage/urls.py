from django.urls import path
from . import views

urlpatterns= [
    path('studentregistration/',views.showformdata),
    
]