from django.shortcuts import render,get_object_or_404, redirect
from .forms import CustomUserCreationForm, SiteInfoForm
from .forms import SiteInfoForm, SiteInfoEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import SiteInfo
from django.core.files.storage import FileSystemStorage
import csv
from django.contrib import messages

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


@login_required
def gestion_csv_view(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Le fichier n\'est pas au format CSV')
            return redirect('gestion_csv')

        csv_data = csv_file.read().decode('utf-8')
        csv_reader = csv.reader(csv_data.splitlines())

        for row in csv_reader:
            if len(row) >= 4:
                site_info = SiteInfo(
                    user=request.user,
                    site_name=row[0],
                    site_url=row[1],
                    username=row[2],
                    password=row[3]
                )
                site_info.save()
        
        return redirect('home')

    return render(request, 'gestionpassword/gestion_csv.html')

@login_required
def delete_site(request, site_id):
    site = get_object_or_404(SiteInfo, pk=site_id)
    if request.user == site.user:
        site.delete()
    return redirect('home')

@login_required
def edit_site(request, site_id):
    site = get_object_or_404(SiteInfo, pk=site_id)

    if request.user != site.user:
        return redirect('home')

    if request.method == 'POST':
        form = SiteInfoEditForm(request.POST, instance=site)  
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SiteInfoEditForm(instance=site) 

    return render(request, 'gestionpassword/edit_site.html', {'form': form, 'site': site})