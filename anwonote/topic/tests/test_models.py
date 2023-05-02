from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from topic.models import Category, Topic

class CategoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testname', password='secret')
        
        self.category = Category(name='test', created_by=self.user)
    
    def test_category_creation(self):
        self.category.save()
        self.assertIsNotNone(self.category.id)

class TopicTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testname', password='secret')
        self.category = Category.objects.create(name='test', created_by=self.user)
        
        self.topic = Topic(category=self.category, name='test', content= 'testcontent', status='Tylko dla mnie',created_at = timezone.now(), created_by=self.user)
    
    def test_category_creation(self):
        self.topic.save()
        self.assertIsNotNone(self.topic.id)
        
        
        