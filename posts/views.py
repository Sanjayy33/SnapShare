from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def create_post(req):
    if req.method == 'POST':
        image = req.FILES.get('image')
        caption = req.POST.get('caption')
        
        Post.objects.create(
                user=req.user,
                image=image,
                caption=caption
            )

        return redirect('home')
    return render(req, 'posts/create_post.html')

@login_required
def home(req):

    posts = Post.objects.all().order_by('-created_at')

    following_user_ids = req.user.following.values_list(
        'following_id',
        flat=True
    )

    for post in posts:
        post.is_liked = post.likes.filter(
            user=req.user
        ).exists()

        post.is_saved = post.saves.filter(
        user=req.user
         ).exists()

    return render(req, 'posts/home.html', {
        'posts': posts,
        'following_user_ids': following_user_ids,
    })

def post_detail(req, id):
    post = Post.objects.get(id=id)
    return render(req, 'posts/post_detail.html',{'posts':post})

def delete_post(req, post_id):
    post = Post.objects.get(id=post_id)

    if post:
        post.delete()

        next_url = req.GET.get('next')
        
        if next_url:
            return redirect(next_url)
        
    return redirect('home')

def notification(req):
    return render(req, 'base.html')