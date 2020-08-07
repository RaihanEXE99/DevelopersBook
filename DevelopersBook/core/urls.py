from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('corelogin/', views.corelogin, name='corelogin'),
    path('corelogout/', views.corelogout, name='corelogout'),
]