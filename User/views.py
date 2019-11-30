from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import UserForm, UserExtraForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def customRegister(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            form_extra = UserExtraForm(form.cleaned_data['filename'])
            form_extra.user = user
            form_extra.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session['user'] = user
            return redirect(reverse('principal:Main'))
        else:
            if len(form.cleaned_data['password']) < 8:
                form.add_error('password', 'La contraseña es muy corta')
            if 'username' in form.errors:
                form.add_error(
                    'username', 'Una cuenta ya ha sido registrada con ese usuario')
            if 'email' in form.errors:
                form.add_error('email', 'Ingresa un correo valido')

            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, template_name='Users/register.html', context=context)
    else:
        context = {
            'form': form,
            'errors': None,
        }

        return render(request, template_name='Users/register.html', context=context)


def customLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['user'] = user
            return redirect(reverse('principal:Main'))
        else:
            context = {
                'form': UserForm(None),
                'errors': True
            }
            return render(request, template_name='Users/login.html', context=context)
    else:
        context = {
            'form': UserForm(None),
            'error': False
        }
        return render(request, template_name='Users/login.html', context=context)


def customLogout(request):
    logout(request)
    del request.session['user']
    return redirect(reverse('principal:Main'))
