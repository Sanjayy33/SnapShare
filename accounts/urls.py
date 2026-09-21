from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/<int:user_id>/',views.profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('search_user/',views.search_user,name='search_user'),
]
