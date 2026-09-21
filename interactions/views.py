from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from posts.models import Post
from notification.models import Notification
from .models import Like, Comment, Save

@login_required
def like_post(req, post_id):
    post = Post.objects.get(id=post_id) 
    like = Like.objects.filter(
        user=req.user,
        post=post
    )

    if like.exists():
        like.delete()
        liked = False

        Notification.objects.filter(
             receiver=post.user,
             sender=req.user,
             notification_type="like",
             posts=post
        ).delete()


    else:
        Like.objects.create(
            user=req.user,
            post=post
        )
        liked = True

        if post.user != req.user:
             Notification.objects.create(
                  receiver=post.user,
                  sender=req.user,
                  notification_type='like',
                  posts=post
             )

    next_url = req.GET.get('next')
    
    if next_url:
        return redirect(next_url)
    
    return redirect('home')

@login_required
def add_comment(req, post_id):
    post = get_object_or_404(Post, id=post_id)

    if req.method=='POST':
        text = req.POST.get('text')
        if text:
            comment = Comment.objects.create(
                user=req.user,
                post=post,
                text=text
            )

            if post.user != req.user:
                Notification.objects.create(
                    receiver=post.user,
                    sender=req.user,
                    notification_type="comment",
                    posts=post,
                    comment=comment
                )

    next_url = req.GET.get('next')
    
    if next_url:
            return redirect(next_url)
    
    return redirect('home')

@login_required
def delete_comment(req, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user==req.user:
         comment.delete()

    next_url = req.GET.get('next')
        
    if next_url:
            return redirect(next_url)
        
    return redirect('home')

@login_required
def save_post(req, post_id):
    post = Post.objects.get(id=post_id)

    saved = Save.objects.filter(
        user=req.user,
        post=post
    )

    if saved.exists():
        saved.delete()

        Notification.objects.create(
            receiver=post.user,
            sender=req.user,
            notification_type="save",
            posts=post  
        ).delete()
    else:
        Save.objects.create(
            user=req.user,
            post=post
        )

        if post.user != req.user:
            Notification.objects.create(
                    receiver=post.user,
                    sender=req.user,
                    notification_type="save",
                    posts=post  
                )

    next_url = req.GET.get('next')
        
    if next_url:
            return redirect(next_url)
        
    return redirect('home')