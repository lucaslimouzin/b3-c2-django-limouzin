from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='gestionpassword/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('add_password/', views.add_password_view, name='add_password'),
    path('gestion_csv/', views.gestion_csv_view, name='gestion_csv'),     
    path('logout/', views.logout_view, name='logout'), 
    path('delete_site/<int:site_id>/', views.delete_site, name='delete_site'),
    path('edit_site/<int:site_id>/', views.edit_site, name='edit_site'),
    path('download_csv/', views.download_csv, name='download_csv'),
]
