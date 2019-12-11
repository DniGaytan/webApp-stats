from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import UserForm, UserExtraForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def customRegister(request):

    if(request.user.is_anonymous):
        this_user = 'Anonymous'
    else:
        this_user = request.user.first_name

    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # form_extra = UserExtraForm(form.cleaned_data['filename'])
            # form_extra.user = user
            # form_extra.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('hub:home'))
        else:
            if len(form.cleaned_data['password']) < 8:
                form.add_error('password', 'La contraseña es muy corta')
            if 'username' in form.errors:
                form.add_error(
                    'username', 'Una cuenta ya ha sido registrada con ese usuario')
            if 'email' in form.errors:
                form.add_error('email', 'Ingresa un correo valido')

            context = {
                'user': this_user,
                'form': form,
                'errors': form.errors,
            }
            return render(request, template_name='User/register.html', context=context)
    else:
        context = {
            'user': this_user,
            'form': form,
            'errors': None,
        }

        return render(request, template_name='User/register.html', context=context)


def customLogin(request):
    if(request.user.is_anonymous):
        this_user = 'Anonymous'
    else:
        this_user = request.user.first_name

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('hub:home'))
        else:
            context = {
                'form': UserForm(None),
                'errors': True
            }
            return render(request, template_name='User/login.html', context=context)
    else:
        context = {
            'user': this_user,
            'form': UserForm(None),
            'error': False
        }
        return render(request, template_name='User/login.html', context=context)


def customLogout(request):
    logout(request)
    return redirect(reverse('user:login'))
