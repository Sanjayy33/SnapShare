from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    ) 

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','post')

class Comment(models.Model):
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE
        )
    
    post = models.ForeignKey(
            Post,
            on_delete=models.CASCADE,
            related_name='comments'
        ) 

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Save(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
            )
        
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='saves'
        ) 
        
    created_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        unique_together = ('user','post')