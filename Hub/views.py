from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:

        # get firstname or username as default
        if(request.user.first_name == ''):
            this_user = request.user.username
        else:
            this_user = request.user.first_name

        context = {
            'user': this_user,
        }

        return render(request, template_name='Hub/home.html', context=context)
    else:
        return redirect(reverse('user:login'))
