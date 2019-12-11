from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now as timeNow


GAME_CHOICES = [
    ('FIFA', 'FIFA'),
    ('SMASH', 'Smash'),
]


class Match(models.Model):
    admin = models.ForeignKey(
        User, related_name='admin', default=1, on_delete=None)
    name = models.CharField(
        max_length=30, default='Match')
    game = models.CharField(
        max_length=10, choices=GAME_CHOICES, default='FIFA')
    date = models.DateField(default=timeNow)


class MatchEntry(models.Model):
    participant = models.ForeignKey(User, on_delete=None)
    match = models.ForeignKey(Match, on_delete=None)
    score = models.BigIntegerField(default=1)
