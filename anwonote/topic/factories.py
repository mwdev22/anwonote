import factory
from factory.random import randgen

from .models import Topic, Category
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    
#   generuje losowe nazwy użytkownika (zgodny z formularzem w aplikacji core)
    username = factory.LazyAttribute(lambda _: ''.join(randgen.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(randgen.randint(5, 20))))
    password = factory.LazyAttribute(lambda _: ''.join(randgen.choice('abcdefghijklmnopqrstuvwxyz123456789#@!$%^&*') for _ in range(randgen.randint(5, 20))))
    class Meta:
        model = User

class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda _: ''.join(randgen.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(randgen.randint(3,35))))
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model=Category



class TopicFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=3)
    content = factory.Faker('text', max_nb_chars=200)
    status = factory.Iterator(['tylko dla mnie', 'dla wszystkich', 'dla zalogowanych'])
    category = factory.SubFactory(CategoryFactory)
    created_by = factory.SubFactory(UserFactory)
    
    class Meta:
        model = Topic
