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
from django.http import HttpResponse

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
        uploaded_file = request.FILES['csv_file']
        if uploaded_file.name.endswith('.csv'):
            data = uploaded_file.read().decode('utf-8').splitlines()

            # Skip the first line (header)
            csv_reader = csv.reader(data)
            next(csv_reader, None)  # Skip the header line

            for line in csv_reader:
                site_name, site_url, username, password = line

                # Check if a site with the same data exists for the current user
                existing_site = SiteInfo.objects.filter(
                    user=request.user,
                    site_name=site_name,
                    site_url=site_url,
                    username=username
                ).first()

                if not existing_site:
                    # Create a new site record
                    new_site = SiteInfo(
                        user=request.user,
                        site_name=site_name,
                        site_url=site_url,
                        username=username,
                        password=password
                    )
                    new_site.save()

            return redirect('home')

    return render(request, 'gestionpassword/gestion_csv.html')

@login_required
def download_csv(request):
    sites = SiteInfo.objects.filter(user=request.user)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sites.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Site Name', 'Site URL', 'Username', 'Password'])

    for site in sites:
        writer.writerow([site.site_name, site.site_url, site.username, site.password])

    return response

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