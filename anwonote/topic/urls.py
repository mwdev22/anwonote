from django.urls import path

from . import views

app_name='topic'

urlpatterns = [
#   dot. postów
    path('filter/', views.filter, name='filter'),
    path('<int:pk>', views.full, name = 'full'),
    path('new_post/', views.new_post, name='new_post'),
    path('delete/<int:pk>', views.delete_post, name='delete_post'),
#   dot. kategorii
    path("new_category/", views.new_category, name='new_category'),
    path('delete_category/', views.delete_category, name='delete_category'),
]
