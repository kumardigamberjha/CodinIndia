from django.shortcuts import render, redirect
import os
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from .models import AddBlog



def index(request):
    return render(request, "website/index.html")

def blog(request):
    blogs = AddBlog.objects.all()
    context = {'blogs': blogs}
    return render(request, "website/blog.html", context)

def readblog(request, post_id):
    blogs = AddBlog.objects.get(pk = post_id)
    read = {'blogs':blogs}

    return render(request, 'website/readblogs.html', read)

def Signup_view(request):
    form = CreateUserForm()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for "+ user+ " succesfully")
            return redirect('login')

    return render(request, 'website/signup.html', {'form':form})
  
def Login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Invalid username/password')

    return render(request, 'website/login.html')

def Logout_view(request):
    logout(request)
    return redirect('login')
