from django.shortcuts import render, redirect
from django.http import HttpResponse
from notification.models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notifications(req):
    notification = Notification.objects.filter(
        receiver=req.user
    ).order_by('-create_at')

    Notification.objects.filter(
        receiver=req.user,
        is_read=False
    ).update(is_read=True)

    return render(req, 'notifications/notification.html',{'notifications':notification})
