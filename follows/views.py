from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Follow
from notification.models import Notification

@login_required
def follow_unfollow(req, user_id):
    target_user = User.objects.get(id=user_id)

    if req.user != target_user:

        follow = Follow.objects.filter(
            follower=req.user,
            following=target_user
        )

        if follow.exists():
            follow.delete()

            Notification.objects.filter(
                receiver=target_user,
                sender=req.user,
                notification_type='follow'
            ).delete()
        else:
            Follow.objects.create(
                follower=req.user,
                following=target_user
            )

            if target_user != req.user:
                Notification.objects.create(
                    receiver=target_user,
                    sender=req.user,
                    notification_type='follow'
                )
    next_url = req.GET.get('next')

    if next_url:
        return redirect(next_url)

    return redirect('home')