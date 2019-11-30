from django.db import models
from django.contrib.auth.models import User


class User_extra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profile_picture = models.FileField()
