from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from user.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'An account was successfully created for {username}')
            register_form.save()
            return redirect('user:register')
        else:
            messages.error(request, f'An account was not created. Check out the red alerts below the fields and try again.')
    else:
        register_form = RegisterForm()
    context = {'register_form': register_form}
    template = 'user/register.html'
    return render(request, template, context)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('blog:index')
        else:
            messages.error(request, f'Username or Password was invalid.')
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    template = 'user/login.html'
    return render(request, template, context)


def logout(request):
    auth_logout(request)
    template = 'user/logout.html'
    return render(request, template)