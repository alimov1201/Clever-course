from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from register.forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect('login')