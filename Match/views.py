from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from Match.models import Match

# Create your views here.


def allMatches(request):
    if request.user.is_authenticated:

        # get all matches
        matches = Match.objects.all()

        if(request.user.first_name == ''):
            this_user = request.user.username
        else:
            this_user = request.user.first_name

        context = {
            'user': this_user,
            'matches': matches,
        }

        return render(request, template_name='./Match/matches.html', context=context)
    else:
        redirect(reverse('user:login'))


def createMatch(request):
    pass


def updateMatch(request, match_id):
    pass


def deleteMatch(request, tournament_id):
    pass


def createTournament(request):
    pass


def updateTournament(request, tournament_id):
    pass


def deleteTournament(request, tournament_id):
    pass
