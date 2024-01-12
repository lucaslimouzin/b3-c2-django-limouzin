from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def login_view(request):
    #logic de connexion
    return render(request, 'gestionpassword/login.html')

def signup_view(request):
    #logic d'inscription
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'gestionpassword/signup.html', {'form': form})