from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_dj
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login_dj(request, user)
            return home(request)
        else:
            return HttpResponse('usuario ou senha inválidos')

@login_required
def home(request):
    return render(request, 'home.html')