from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add extra fields if needed (bio, photo, etc.)

    def __str__(self):
        return self.user.username

