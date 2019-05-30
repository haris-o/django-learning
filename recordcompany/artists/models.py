from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    label = models.ForeignKey('labels.Label', on_delete=models.CASCADE)
