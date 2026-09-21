from .models import Notification

def notification_count(req):
    if req.user.is_authenticated:
        count = Notification.objects.filter(
            receiver=req.user,
            is_read=False
        ).count()


        return {'unread_notification':count}

    return {
        'unread_notification':0
    }
