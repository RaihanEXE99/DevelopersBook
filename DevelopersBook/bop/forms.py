from django import forms

from projects.models import Project
from .models import Notification

class ProjectForm(forms.ModelForm):
    OPTIONS = (
        ("Web_Development" , "Web_Development"),
        ("App_Development" , "App_Development"),
        ("Game_Development" , "Game_Development"),
        ("Software_Development" , "Software_development"),
        ("Graphic_Design", "Graphic_Design"),
        ("Bussiness_Management", "Bussiness_Management"),
        ("Study_And_Assignment", "Study_And_Assignment"),
        ("Script" , "Script"),
        ("Other" , "Other"),
    )
    catagory = forms.ChoiceField(choices=OPTIONS,widget=forms.Select(attrs={
    "class": "text-gray-600 block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline",
    }
    ))
    projectName = forms.CharField(max_length=40, label='Project Name', widget=forms.TextInput(attrs={

    "class" : "w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
    "type" : "text",
    "placeholder": "Your project name ?"
    
    }))
    Details = forms.CharField(widget=forms.Textarea(attrs={
        "class": "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
        "placeholder": "Add requirements ....",
        "rows" : "2"
    }))
    Requirements = forms.CharField(widget=forms.Textarea(attrs={
        "class": "w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
        "placeholder": "Add requirements ....",
        "rows" : "2"
    }))
    
    
    
    

    class Meta:
        model = Project
        fields = ('catagory', 'projectName', 'Details', 'Requirements')
        

class NotificationForm(forms.ModelForm):
    projectName = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Notification
        fields = ('projectName',)