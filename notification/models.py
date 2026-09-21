from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from interactions.models import Comment

class Notification(models.Model):
    NOTIFICATION_TYPE = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow'),
        ('save','Save'),
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_notification'
    )

    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPE
    )

    posts = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )

    is_read = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({self.notification_type})"