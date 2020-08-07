from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from projects.models import Project
from .models import biox,Notification
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

import asyncio,time

# Create your views here.
@login_required(login_url="/core/corelogin/")
def createProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Cadmin = request.user
            post.save()
            post.Cusers.add(request.user)
            # print(request.user.id)
            # return render(request, 'bop/profile.html')
            return redirect('bop:profile')
    form = ProjectForm()
    # time.sleep(2)
    return render(request, 'bop/createProject.html',{'form': form})


@login_required(login_url="/core/corelogin/")
def profile(request):
    projectlist = Project.objects.filter(Cusers__username=request.user)
    bio = biox.objects.filter(Cuser=request.user)
    print(bio)
    print(projectlist)
    return render(request, 'bop/profile.html', {
        'u': request.user,
        'p': projectlist,
        'b': bio
    })

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Cadmin = request.user
            post.Cusers.add(User.objects.get(id=request.user.id))
            post.save()
            print("Created New project",post)
            return render(request, 'bop/profile.html')
    form = ProjectForm()
    return render(request, 'bop/profile.html')

def LetMeIn(request, that_id):
    # that_project = Project.objects.get(id=that_id)
    if request.method == "POST":
        message = request.POST['message']
        projectName = Project.objects.get(id=that_id)
        toAdmin = projectName.Cadmin
        reqUser = request.user
        done = Notification(projectName=projectName, reqUser=reqUser, message=message,toAdmin=toAdmin)
        done.save()
        print(message,projectName,reqUser)
        return redirect('bop:profile')
    return render(request, 'bop/LetMeIn.html', {
        'that_id' : that_id
    })


@login_required(login_url="/core/corelogin/")
def MyNotification(request):
    myN = Notification.objects.filter(toAdmin=request.user.username)
    counter = 0
    for x in myN:
        counter += 1
    if counter == 0:
       return render(request, 'bop/MyNotification.html') 
    return render(request, 'bop/MyNotification.html',
    {
        'myN' : myN
    })


@login_required(login_url="/core/corelogin/")
def myProjects(request):
    projectlist = Project.objects.filter(Cusers__username=request.user)
    counter = 0
    for x in projectlist:
        counter += 1
        print(x)
    return render(request, 'projects/myProjects.html', {
        'u': request.user,
        'p': projectlist,
        'counter' : counter
    })


def update(request):
    if request.method == "POST":
        Cuser = request.user
        userBio = request.POST['userBio']
        myGit = request.POST['myGit']
        myFb = request.POST['myFb']
        try:
            done = biox(Cuser=Cuser, userBio=userBio, myGit=myGit,myFb=myFb)
            done.save()
        except:
            biox.objects.filter(Cuser=request.user).update( userBio=userBio, myGit=myGit,myFb=myFb)
        return redirect('bop:profile')
    
    that_bio = biox.objects.filter(Cuser=request.user)
    return render(request, 'bop/Update.html', {
        'that_bio' : that_bio
    })



@login_required(login_url="/core/corelogin/")
def NotificationDecision(request,that_id):
    if request.method == "POST":
        decision = request.POST['decision']
        # print("1")
        if decision == "Reject":
            that_notification = Notification.objects.get(id=that_id)
            that_notification.delete()
            # reverse
            return redirect('bop:MyNotification')
        if decision == "Accept":
            that_notification = Notification.objects.get(id=that_id)
            that_project = Project.objects.get(id=that_notification.projectName.id)
            that_user = User.objects.get(username=that_notification.reqUser)
            that_project.Cusers.add(that_user)
            that_notification.delete()

            return redirect('bop:MyNotification')

def users(request):
    all_accounts = SocialAccount.objects.filter()
    print(all_accounts)
    for x in all_accounts:
        print(x.extra_data)
    return render(request, 'bop/users.html', {
        'all_accounts' : all_accounts
    })

def thatUser(request, that_username):
    that_user = User.objects.get(username=that_username)
    social = SocialAccount.objects.get(user = that_user)
    that_bio = biox.objects.filter(Cuser=that_user)
    try:
        print("try")
        that_bio = that_bio[0]
        print(social.uid)
        return render(request, 'bop/thatUser.html', {
        'that_user' : that_user,
        'that_bio': that_bio,
        'social' : social
    })
    except:
        print("except")
        pass
    print(that_user,that_bio,social.uid)
    return render(request, 'bop/thatUser.html', {
        'that_user' : that_user,
        # 'that_bio': that_bio,
        'social' : social
    })
