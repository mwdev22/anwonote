from django.contrib import admin

from .models import Category, Topic


# rejestrowanie tabeli bazy danych na stronie admina
admin.site.register(Category)
admin.site.register(Topic)