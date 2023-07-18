from django.shortcuts import redirect, render
from requests import request
from .models import Post
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password )

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, 'Username OR password is incorrect')
                


        context = {}
        return render(request, 'base/login.html', context)


def signUpPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save() 
                user = form.cleaned_data.get('username')
                messages.success(request, "Account is Created for " + user) 
                redirect('login-user')

        context = {'form' : form}
        return render(request, 'base/sign_up.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login-user')

@login_required(login_url='login-user')
def home(request):
    posts = Post.objects.all()
    context ={'posts':posts}
    return render(request, 'base/home.html', context)

@login_required(login_url='login-user')
def add(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['description']
        Post.objects.create(
            title = title,
            description = desc,
        ),
        messages.success(request, "Post has been added to the data base")
        return redirect('home')
    # context = {'messages':messages}
    return render(request, 'base/add.html')


@login_required(login_url='login-user')
def update(request, pk):

    post = Post.objects.get(id = pk)

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
        Post.objects.filter(id=pk).update(
            title = title,
            description = desc,
        ),
        messages.success(request, "Post has been Updated") 
        return redirect('home')


    context = {'post' : post}
    return render(request, 'base/update.html', context)

@login_required(login_url='login-user')
def delete(request, pk):
    Post.objects.filter(id = pk).delete()
    
    return redirect('/')  