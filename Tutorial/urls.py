from django.contrib import admin
from django.urls import path
from .views import tutorial_create,tutorial_display,tutorial_like

urlpatterns = [
    path('create/' , tutorial_create , name = 'create_tutorial'),
    path('display/' , tutorial_display , name = 'display_tutorial'),
    path('<int:tpk>/likes/',tutorial_like , name = 'likes_tutorial'),
]