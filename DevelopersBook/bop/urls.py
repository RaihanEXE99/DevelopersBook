from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'bop'

urlpatterns = [
    path('thatUser/<str:that_username>',views.thatUser,name="thatUser"),
    path('users/',views.users,name="users"),
    path('update/',views.update,name="update"),
    path('myProjects/',views.myProjects,name="myProjects"),
    path('createProject/', views.createProject, name='createProject'),
    path('MyNotification/', views.MyNotification, name='MyNotification'),
    path('profile/', views.profile, name='profile'),
    path('project_new/', views.project_new, name='project_new'),
    path('LetMeIn/<int:that_id>', views.LetMeIn, name='LetMeIn'),
    path('NotificationDecision/<int:that_id>',views.NotificationDecision,name='NotificationDecision')
]