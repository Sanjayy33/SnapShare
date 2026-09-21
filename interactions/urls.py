from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:post_id>/',views.like_post,name='like_post'),
    path('comment/<int:post_id>/',views.add_comment,name='add_comment'),
    path('comment_delete/<int:comment_id>/',views.delete_comment,name='delete_comment'),
    path('save/<int:post_id>/',views.save_post,name='save_post'),
]
