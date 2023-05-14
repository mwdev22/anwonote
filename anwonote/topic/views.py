from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Topic, Category
from .forms import NewPostForm,NewCategoryForm

# filtrowanie
def filter(request):
    category_id = request.GET.get('category')
    if category_id:
    #   Wyświetlanie postów według filtrów
        if request.user.is_authenticated:
            topics = Topic.objects.filter(
            Q(status='dla wszystkich') & Q(category_id=category_id)
            | Q(created_by=request.user) & Q(category_id=category_id)
            | Q(status='dla zalogowanych') & Q(category_id=category_id)
        )
        else:
            topics = Topic.objects.filter(status='dla wszystkich')
    else:
        return redirect('/')
    categories = Category.objects.all()
    page = Paginator(topics, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'categories':categories,
        'page':page,
    }
    return render(request, 'topic/filter.html', context)

# podgląd postu
def full(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request,'topic/full.html',{
        'topic':topic,
    })

# nowy post

def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
    # commit=False daje możliwość zmiany dowolnego atrybutu rekordu przed jego zapisaniem w bazie
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'topic/forms.html', {
        'form':form,
    })

# usunięcie posta

def delete_post(request, pk):
    post_to_delete = Topic.objects.get(pk=pk)
#   usuwanie posta
    post_to_delete.delete()
    return redirect('/')

# nowa kategoria

def new_category(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('/')
    else:
        form = NewCategoryForm()
    return render(request, 'topic/forms.html', {
        'form':form,
    })

# usunięcie kategorii

def delete_category(request):
    category_id= request.POST.get('category_id')
    category_to_delete = Category.objects.get(pk=category_id)
    category_to_delete.delete()
    return redirect('/')
