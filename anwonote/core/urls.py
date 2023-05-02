from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Logowanie.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.Wylogowanie.as_view(template_name='core/logout.html'), name='logout'),
]