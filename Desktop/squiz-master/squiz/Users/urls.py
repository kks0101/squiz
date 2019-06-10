from django.urls import path
from . import  views

app_name = "Users"

urlpatterns = [
    path('profile/', views.profile, name='profile_info'),
    path('leaderboard/<int:pk>/', views.leaderboard, name='leaderboard'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register, name='signup'),
    path('', views.home, name="home")
]