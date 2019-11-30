from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def getHome(request):
    if request.user.is_authenticated:
        return render(request, template_name='Hub/home.html')
    pass
