from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.home_view, name='home'),
    path('add_password/', views.add_password_view, name='add_password'),
    path('view_all/', views.view_all_passwords_view, name='view_all'),  
    path('logout/', views.logout_view, name='logout'), 
]
