from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json
import topic.views as views
from topic.models import Category, Topic


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.filter_url = reverse('topic:filter')
        self.new_category_url = reverse('topic:new_category')
        self.new_post_url = reverse('topic:new_post')

        self.user = User.objects.create_user(username='usertest', email='test@example.com', password='testpass')

    def test_filter_GET_nocatid(self):
        response = self.client.get(self.filter_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('topic/filter.html')
    
    def test_full_GET(self):
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='example', created_by=user)
        topic = Topic.objects.create(category=category, created_by=user)
        full_url = reverse('topic:full', args=[topic.id])
        response = self.client.get(full_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('topic/full.html')

    def test_new_post_GET(self):
        response = self.client.get(self.new_post_url)
        self.assertTemplateUsed('topic/forms.html')
        self.assertEqual(response.status_code, 200)
    
    def test_new_post_POST(self):
        category = Category.objects.create(name='testcat', created_by=self.user)
        response = self.client.post(self.new_post_url, {
            'category':category.name,
            'name':'testname',
            'content':'testcontent',
            'status':'Tylko dla mnie'
        })
        self.assertEqual(response.status_code, 200)

    def test_new_category_GET(self):
        response = self.client.get(self.new_category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('topic/forms.html')
    
   
        