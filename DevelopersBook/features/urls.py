from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'features'

urlpatterns = [
    path('HtmlEditor/', views.HtmlEditor, name='HtmlEditor'),
    path('ScreenRecorder/', views.ScreenRecorder, name='ScreenRecorder'),
    path('DrawIo/', views.DrawIo, name='DrawIo'),
    path('FileUpload/',views.fileUpload,name='fileUpload')
]