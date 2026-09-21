from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='posts/'
    )

    caption = models.TextField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username