from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, SiteInfoForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import SiteInfo

def login_view(request):
    #logic de connexion
    return render(request, 'gestionpassword/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'gestionpassword/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    #logic home
    sites = SiteInfo.objects.filter(user=request.user)
    return render(request, 'gestionpassword/home.html', {'sites': sites})

@login_required
def add_password_view(request):
    if request.method == 'POST':
        form = SiteInfoForm(request.POST)
        if form.is_valid():
            site_info = form.save(commit=False)
            site_info.user = request.user 
            site_info.save()
            return redirect('home')  
    else:
        form = SiteInfoForm()
    return render(request, 'gestionpassword/add_password.html', {'form': form})


def view_all_passwords_view(request):
    #logic view all
    return render(request, 'gestionpassword/view_all.html')