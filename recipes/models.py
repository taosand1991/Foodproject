from django.db import models
from django.shortcuts import reverse
from accounts.models import Profile
from django.conf import settings
from django.contrib.auth.models import User


class Movie(models.Model):
    movie = models.CharField(max_length=50)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.movie

    def get_absolute_url(self):
        reverse('delete', args=[self.pk])

