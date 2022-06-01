from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
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


