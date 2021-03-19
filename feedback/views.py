from django.shortcuts import render
from .models import Feedback

from django.http import HttpResponseRedirect
# Create your views here.

def feedback_create(request):
    context = {}
    context['valid'] = True
    user = request.user
    if user.is_active:
        if request.method == 'POST':
            username = request.POST['username']
            thoughts = request.POST['thoughts']
            question1 = request.POST['question1']
            question2 = request.POST['question1']
            question3 = request.POST['question1']
            question4 = request.POST['question1']

            image = request.FILES['image']
            print(image)
            Feedback.objects.create( feedback_uploader=user,username=username , image=image , thoughts = thoughts  , question1 = question1 , question2 = question2 ,question3 = question3 , question4= question4)
        print('success')
    else:
        context['valid'] = False
    return render(request , 'Feedback/feedback_create.html' , context)


def feedback_display(request):
    context = {}
    user = request.user
    context['valid'] = True
    if user.is_active:
        feedbacks = Feedback.objects.all()
        print(feedbacks[0].feedback_uploader)
        context['feedbacks'] = feedbacks
    return render(request , 'Feedback/feedback_display.html' , context)