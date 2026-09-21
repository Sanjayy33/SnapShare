from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from follows.models import Follow
from posts.models import Post

@login_required
def profile(req, user_id):
    user = get_object_or_404(User, id=user_id)

    profile, created = Profile.objects.get_or_create(
        user=user
    )

    posts = Post.objects.filter(user=user).order_by('-created_at')

    following_user_ids = req.user.following.values_list(
        'following_id',
        flat=True
    )
    for post in posts:
        post.is_liked = post.likes.filter(user=req.user).exists()
        post.is_saved = post.saves.filter(user=req.user).exists()

    followers = user.followers.all()
    following = user.following.all()
 
    return render(req, 'accounts/profile.html', {
        'user': user,
        'posts': posts,
        'profile': profile,
        'following_user_ids': following_user_ids,
        'followers':followers,
        'followings':following
    })


def register(req):

    if req.method == "POST":

        username = req.POST.get("username")
        phone = req.POST.get("phone")
        email = req.POST.get("email")
        password = req.POST.get("password1")
        password2 = req.POST.get("password2")

        if password != password2:
            return render(
                req,
                "accounts/register.html",
                {"error": "Password does not match"}
            )

        if User.objects.filter(username=username).exists():
            return render(
                req,
                "accounts/register.html",
                {"error": "User already exists"}
            )

        if User.objects.filter(email=email).exists():
            return render(
                req,
                "accounts/register.html",
                {"error": "Email already exists"}
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(
            user=user,
            phone=phone
        )

        return redirect("login")

    return render(req, "accounts/register.html")

def login_user(req):
    if req.method=="POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(
            req,
            username=username,
            password=password
        )

        if user is not None:
            login(req,user)
            return redirect("home")

        return render(req,"accounts/login.html",{'error':'invalid username or passowrd'})
    return render(req, 'accounts/login.html')

def logout_user(req):
    logout(req)
    return redirect("home")


@login_required
def update_profile(req):

    if req.method == 'POST':

        username = req.POST.get('username')
        bio = req.POST.get('bio')
        profile_image = req.FILES.get('profile_image')

        user = req.user

        if username:
            user.username = username
            user.save()

        profile, created = Profile.objects.get_or_create(
            user=user
        )

        profile.bio = bio

        if profile_image:
            profile.profile_image = profile_image

        profile.save()

    return redirect('profile', user_id=req.user.id)

def search_user(req):
    query = req.GET.get('q','')
    users = User.objects.filter(
        username__icontains=query
    )
    return render(req, 'accounts/search_user.html',
                  {'users':users,'query':query})