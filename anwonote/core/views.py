from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from topic.models import Category, Topic
from .forms import SignupForm


# strona tytułowa
def index(request):
    topics = Topic.objects.all()
    categories = Category.objects.all()
    page = Paginator(topics, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    
    return render(request, 'core/index.html',{
        'categories':categories,
        'page':page,
        'topics':topics,
    })
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            form = SignupForm()

    return render(request, 'core/signup.html',{
        'form' : form
    })

