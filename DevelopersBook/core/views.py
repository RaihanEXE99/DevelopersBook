from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount


# Create your views here.
def corelogin(request):
    # u = User.objects.get(username = request.user)
    # print(u.socialaccount.uid)
    try:
        su = SocialAccount.objects.get(user = request.user)
        print(su.uid)
        return render(request, 'core/corelogin.html', {
            'su':su
        })
    except:
        return render(request, 'core/corelogin.html', {
        })

@login_required(login_url="/core/corelogin/")
def corelogout(request):
    logout(request)
    return redirect('/')

# @login_required(login_url="/core/corelogin/")
# def forTest(request):
#     su = SocialAccount.objects.all()
#     u = User.objects.all()
#     for susu in su:
#         print(susu)
#     return render(request, 'core/forTest.html', {
#         # 'su': su,
#         # 'u' : u
#     })


