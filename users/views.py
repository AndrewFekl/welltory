from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm


def registerUser(request):

    page = 'register'
    form = UserCreationForm()
    #form = CustomUserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('main-page')
        else:
            messages.success(request, 'An error has accurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
