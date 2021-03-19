from django.contrib import admin
from .models import Feedback
# Register your models here.
@admin.register(Feedback)

class feedbackAdmin(admin.ModelAdmin):
    list_display=('id','username','thoughts','question1','question2','question3','question4')