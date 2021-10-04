from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url="/core/corelogin/")
def projectList(request):
    projectlist = Project.objects.all()
    return render(request, 'Projects/projectList.html',{
        'projectlist' : projectlist
    })

@login_required(login_url="/core/corelogin/")
def seeProject(request, that_id):
    that_project = Project.objects.get(id=that_id)
    print(that_project)
    return render(request, 'projects/seeProject.html',
    {
        "that_project" : that_project
    })


