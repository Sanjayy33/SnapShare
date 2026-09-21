from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='profile_img/',
        default='profile_img/user.png',
        blank=True,
    )

    bio = models.TextField(max_length=180,blank=True)

    def __str__(self):
        return self.user.username