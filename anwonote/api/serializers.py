from rest_framework import serializers
from django.contrib.auth.models import User
from topic.models import Topic, Category


# lista użytkowników
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Category
        fields = ['id' ,'name', 'created_by']

class TopicSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Topic
        fields = ['id' ,'name', 'content', 'status', 'created_at', 'created_by']
        
