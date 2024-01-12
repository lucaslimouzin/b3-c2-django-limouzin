from django.shortcuts import render, redirect

def login_view(request):
    #logic de connexion
    return render(request, 'gestionpassword/login.html')

def signup_view(request):
    #logic d'inscription
    return render(request, 'gestionpassword/signup.html')