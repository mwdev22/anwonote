from rest_framework import generics
from .serializers import TopicSerializer, CategorySerializer, UserSerializer
from .serializers import Topic,Category,User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.filter(status='dla wszystkich')
    serializer_class = TopicSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer