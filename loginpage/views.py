from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import reverse
from .forms import StudentRegistration
from loginpage.models import Client
# Create your views here.



"""def showformdata(request):
    if request.method =='POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            un = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            tex=fm.cleaned_data['discription']

            reg = User(username=un, email=em , password=pw,discription=tex)
            reg.save()

            return render(request,'loginpage/success.html',{'name': un})
    else:
        fm=StudentRegistration()

    fm= StudentRegistration(auto_id=True)
    return render(request,'signup.html',{'form':fm})"""


def user_signup(request):
    context = {}
    context['valid'] = True
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        description = request.POST['description']
        password = request.POST['password']
        is_mentor = request.POST['mentor']
        pass2 = request.POST['pass2']
        print(is_mentor == 'on')
        if password == pass2:
            if is_mentor == 'on':
                Client.objects.create(username=username , email=email , discription=description , password=password , is_mentor=True)
            else:
                Client.objects.create(username=username , email = email , password = password , description = description , is_mentor=False)
            return HttpResponseRedirect(reverse('login'))
            print('success')
        else:
            context['valid'] = False
            context['message'] = 'Please check your passwords again'
    return render(request , 'loginpage/signup.html' , context)

def user_login(request):
    context = {}
    context['valid'] = True
    user = request.user
    if not user.is_active:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username , password = password)
            if user is not None:
                auth.login(request , user)
                return HttpResponseRedirect(reverse('login'))
            else:
                context['valid'] = False
                context['messages'] = 'Please check your Username and Password again.'
                return HttpResponseRedirect(reverse('login'))
    return render(request , 'loginpage/login.html' , context)

def user_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect(reverse('login'))