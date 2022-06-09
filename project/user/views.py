from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from user import models as user_models
from user.forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm


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
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:question-index')
        else:
            messages.error(request, f'Username or Password was invalid.')
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    template = 'user/login.html'
    return render(request, template, context)


def logout(request):
    username = request.user
    auth_logout(request)
    context = {'username': username}
    template = 'user/logout.html'
    return render(request, template, context)


@login_required(redirect_field_name='next')
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'You profile has been updated')
            return redirect('user:profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        if not hasattr(request.user, 'profile'):
            user_models.Profile.objects.create(user=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    template = 'user/profile.html'
    return render(request, template, context)
 