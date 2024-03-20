from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_dj, logout as logout_dj
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(password)
    user = authenticate(username=username, password=password)
    if user:
        login_dj(request, user)
        return redirect("home")
    else:
        messages.success(request, ("Usuário ou senha inválidos."))
        return redirect('/users/login')



def logout(request):
    logout_dj(request)
    return redirect('/users/login')

@login_required
def user_settings(request):
    if request.method == "GET":
        return render(request, 'user_settings.html')
    user = request.user
    user.first_name = request.POST.get('firstName')
    user.last_name = request.POST.get('lastName')
    user.email = request.POST.get('email')
    user.save()
    return redirect('users:user_settings')