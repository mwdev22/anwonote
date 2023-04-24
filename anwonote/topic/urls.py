from django.urls import path

from . import views

app_name='topic'

urlpatterns = [
    path('new/', views.new, name='new'),
    path("newCategory/", views.newCategory, name='newCategory'),
    path('<int:pk>', views.full, name = 'full'),
    path('filter/', views.filter, name='filter'),
    path('delete/<int:pk>', views.delete_post, name='delete_post'),
    path('delete_category/', views.delete_category, name='delete_category'),
]
