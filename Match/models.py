from django.db import models
from django.contrib.auth.models import User

GAME_CHOICES = (
    ('fifa', 'FIFA'),
    ('mk', 'Mortal Kombat'),
)


class Tournament(models.Model):
    name = models.CharField(max_length=50, default='No name')


class TournamentParticipants(models.Model):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Match(models.Model):
    match_admin = models.ForeignKey(
        User, related_name='admin', on_delete=None, default=1)
    player_one = models.ForeignKey(
        User, related_name='player_one', on_delete=None, default=1)
    player_two = models.ForeignKey(
        User, related_name='player_two', on_delete=None, default=1)
    game = models.CharField(
        max_length=15, choices=GAME_CHOICES, default='fifa')
    result_player_one = models.IntegerField(default=0)
    result_player_two = models.IntegerField(default=0)
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, default=1)
