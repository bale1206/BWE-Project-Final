from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import UserForm
from .models import User
from django.contrib.auth import login as auth_login

def index(request):
    context = {}
    return render(request,'pages/index.html', context)

def explorer(request):
    context = {}
    return render(request,'pages/explorer.html', context)

def login(request):
    context = {}
    return render(request,'pages/login.html', context)

def profile(request):
    context = {}
    return render(request,'pages/profile.html', context)

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            auth_login(request, user)  # Log the user in after registration
            messages.success(request, 'Account created successfully')
            return redirect('index')  # Redirect to a page of your choice
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'form': form})



def shoppingcart(request):
    context = {}
    return render(request,'pages/shoppingcart.html', context)

def plans(request):
    context = {}
    return render(request, 'pages/plans.html', context)

def usr(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=UserForm()
    return render(request, 'pages/crud.html', {'form':form})

def show(request):
    users = User.objects.all()
    return render(request, 'pages/show.html', {'users': users})

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'pages/edit.html', {'user': user})

def update(request, id):
    user = User.objects.get(id=id)
    form=UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'pages/edit.html', {'user': user})

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/show")
    