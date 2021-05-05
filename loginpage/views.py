from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import reverse
from loginpage.models import Client
# Create your views here.


def user_signup(request):
    context = {}
    context['valid'] = True
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        description = request.POST['description']
        password = request.POST['password']
        pass2 = request.POST['pass2']
        try: 
            if request.POST['mentor'] is not None:
                is_mentor = True
                print('in try')
            else:
                is_mentor = False
                print('in catch')
        except:
            is_mentor = False
            print('in try catch')
        if password == pass2 and password != '':
            if is_mentor:
                print('in is mentro if')
                user = User.objects.create_user(username=username, email=email, password=password)
                Client.objects.create(user = user ,description=description, is_mentor=True)
            else:
                print('in is mentor else')
                user = User.objects.create_user(username=username, email=email, password=password)
                Client.objects.create(user = user ,description=description, is_mentor=False)
            print('success')
            return HttpResponseRedirect(reverse('login'))
        else:
            print('Fail')
            context['valid'] = False
            context['message'] = 'Please check your passwords again'
            return HttpResponseRedirect(reverse('signup'))
    else:
        print('No POST')
    return render(request , 'loginpage/signup.html' , context)

def user_login(request):
    context = {}
    context['valid'] = True
    user = request.user
    if not user.is_active:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                print('success')
                return HttpResponseRedirect(reverse('home'))
            else:
                print('Fail')
                context['valid'] = False
                context['messages'] = 'Please check your Username and Password again.'
                return HttpResponseRedirect(reverse('login'))
    else:
        print('user is active')
    return render(request , 'signup.html' , context)

def user_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect(reverse('login'))