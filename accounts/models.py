from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    location = models.CharField(max_length=50)
    biography = models.TextField(blank=True)
    image_cover = models.ImageField(upload_to='img/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name




