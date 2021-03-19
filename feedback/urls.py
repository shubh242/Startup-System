from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/' , views.feedback_create , name = 'create_feedback'),
    path('display/' , views.feedback_display , name = 'display_feedback'),
    
]