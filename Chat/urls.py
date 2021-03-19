from django.contrib import admin
from django.urls import path
from .views import message_list , messages_api , contacts_list


urlpatterns = [
    path('<int:pk>/', messages_api, name="messages_api"),
    path('view/<int:pk>/', message_list, name="message_list"),
    path('list/', contacts_list, name="contact_list"),
] 