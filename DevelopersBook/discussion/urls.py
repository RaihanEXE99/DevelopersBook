from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'discussion'

urlpatterns = [
    path('inDiscussion/<int:that_discussion_id>/', views.inDiscussion, name="inDiscussion"),
    path('', views.discussionList, name="discussionList"),
    path('replyDiscussion/<int:that_discussion_id>/',views.replyDiscussion,name="replyDiscussion")
    
]