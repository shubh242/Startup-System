from django.shortcuts import render

from .forms import StudentRegistration
from .models import User
# Create your views here.



def showformdata(request):
    if request.method =='POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            un = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(username=un, email=em , password=pw)
            reg.save()

            return render(request,'loginpage/success.html',{'name': un})
    else:
        fm=StudentRegistration()

    fm= StudentRegistration(auto_id=True)
    return render(request,'loginpage/userregistration.html',{'form':fm})