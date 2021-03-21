from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("SignUp/", views.Signup_view, name="signup"),
    path('login/', views.Login_view, name="login"),
    path('logout/', views.Logout_view, name="logout"),
    path('readblog/<post_id>/', views.readblog, name="readblog"),
]