from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from patient.models import Patient
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html', {'msg': 'wlcm'})
    context = {
        'user': request.user
    }
    return render(request, 'users/user.html', context)


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'users/login.html', {'msg':'invalid credentials'})

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'msg':'logged out'})

