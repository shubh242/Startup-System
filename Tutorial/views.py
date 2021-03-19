from django.shortcuts import render
from Tutorial.models import Tutorial
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def tutorial_create(request):
    context = {}
    context['valid'] = True
    user = request.user
    if user.is_active:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            tags = request.POST['tags']
            video = request.FILES['video']
            print(video)
            Tutorial.objects.create(tutorial_uploader=user , tutorial_title=title , tutorial_description = description , tutorial_tags = tags , tutorial_video = video)
        print('success')
    else:
        context['valid'] = False
    return render(request , 'tutorial/tutorial_create.html' , context)


def tutorial_display(request):
    context = {}
    user = request.user
    context['valid'] = True
    if user.is_active:
        tutorials = Tutorial.objects.all()
        print(tutorials[0].tutorial_uploader)
        context['tutorials'] = tutorials
    return render(request , 'tutorial/tutorial_display.html' , context)

def tutorial_like(request,tpk):
    context = {}
    tutorial = Tutorial.objects.get(id = tpk)
    user = request.user
    context['valid'] = True
    if user.is_active:
        if user in tutorial.tutorial_like.all():
            tutorial.tutorial_like.remove(user)
        else:
            tutorial.tutorial_like.add(user)
    return HttpResponseRedirect(reverse('display_tutorial'))
