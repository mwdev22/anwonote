from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

from topic.models import Category, Topic
from .forms import SignupForm


# strona tytułowa
def index(request):
    topics = Topic.objects.all()
    categories = Category.objects.all()
    page = Paginator(topics, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'categories':categories,
        'page':page,
        'topics':topics,
    }
    return render(request, 'core/index.html', context)
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            form = SignupForm()

    return render(request, 'core/signup.html',{
        'form' : form
    })
    

# !!! przesyłanie cookies podczas logowania !!!
class Logowanie(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        remember_me = self.request.POST.get('remember_me')
        if remember_me == 'true':
            response.set_cookie('remember_me', True, max_age=3600*24*7)
            response.set_cookie('username', form.cleaned_data['username'])
            response.set_cookie('login_status', True)
        return response
    
class Wylogowanie(LogoutView):
#   Funkcja usuwa pliki cookie po wylogowaniu 
    def dispatch(self, request):
        response = super().dispatch(request)
#   Usuwanie cookies po nazwie 
        response.delete_cookie('username')
        response.delete_cookie('login_status')
        response.delete_cookie('remember_me')
        return response