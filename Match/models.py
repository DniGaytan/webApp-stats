from django.db import models
from django.contrib.auth.models import User


GAME_CHOICES = [
    ('FIFA', 'FIFA'),
    ('SMASH', 'Smash'),
]


class Match(models.Model):
    participants = models.ManyToManyField(User)
    admin = models.ForeignKey(
        User, related_name='admin', default=1, on_delete=None)
    participant1Score = models.BigIntegerField()
    participant2Score = models.BigIntegerField()
    game = models.CharField(
        max_length=10, choices=GAME_CHOICES, default='FIFA')
