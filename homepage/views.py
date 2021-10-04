from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView


# Create your views here.

@login_required(login_url="/core/corelogin/")
def homepage(request):
    return render(request, 'homepage/homepage.html')
    
def my_signup(request):
    return render(request, 'homepage/my_signup.html')

def inactive(request):
    return render(request, 'homepage/banned.html')