from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('seeProject/<int:that_id>', views.seeProject, name='seeProject'),
    path('projectList/',views.projectList,name='projectList')
]