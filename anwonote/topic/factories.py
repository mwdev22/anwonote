import factory
from factory.random import randgen

from .models import Topic
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class meta:
        model = User
# generuje losowe nazwy użytkownika (zgodny z formularzem w aplikacji core)
    username = factory.LazyAttribute(lambda _: ''.join(randgen.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(randgen.randint(5, 20))))

class CategoryFactory(factory.django.DjangoModelFactory):
    ...

class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic
    
    name = factory.Faker('sentence', nb_words=3)
    content = factory.Faker('text', max_nb_chars=200)
    status = factory.Iterator(['tylko dla mnie', 'dla wszystkich', 'dla zalogowanych'])
    category = factory.SubFactory(CategoryFactory)
    created_by = factory.SubFactory(UserFactory)