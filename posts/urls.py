from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create-post/',views.create_post,name='create_post'),
    path('delete-post/<int:post_id>/',views.delete_post,name='delete_post'),
    path('post-detail/',views.post_detail,name='post_detail'),
    path('notification/',views.notification,name='notification'),
]
