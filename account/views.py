from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("login")
                login(request, user)
                return redirect('pro:custom_login')
            else:
                message = {'error': 'invalid credentials'}
                context = message
                return render(request, 'login.html', context)
            # if user is not None:
            #     login(request, user)
            #     return redirect('job:list')  # Redirect to home page after successful login
            # else:
            #     # Handle invalid login
            #     return render(request, 'login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('account:login')
