from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Topic, Category
from .forms import NewPostForm,NewCategoryForm

# filtrowanie
def filter(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    if category_id:
        topics = Topic.objects.filter(category_id=category_id)
    else:
        topics = Topic.objects.all()
        return redirect('/')
    page = Paginator(topics, 9)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'topics':topics,
        'categories':categories,
        'page':page,
        'default':category_id
    }
    return render(request, 'topic/filter.html', context)

# konkretny post 
def full(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request,'topic/full.html',{
        'topic':topic,
    })

# nowy post
@login_required
def new(request):
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
@login_required
def delete_post(request, pk):
    post_to_delete = Topic.objects.get(pk=pk)
#   na żądanie klienta posty są archiwizowane a nie usuwane, aby miał wgląd na posty usuwane przez jego pracowników
    post_to_delete.status = 'Ukryty'
    post_to_delete.save()

    return redirect('/')

@login_required
def newCategory(request):
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

@login_required
def delete_category(request):
    category_id= request.POST.get('category_id')
    category_to_delete = Category.objects.get(pk=category_id)
    category_to_delete.delete()
    return redirect('/')
