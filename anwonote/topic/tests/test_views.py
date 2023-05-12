from django.test import TestCase, Client
from django.urls import reverse
import json
from random import randint

import topic.views as views
from topic.models import Category, Topic
from .test_urls import topics_count, category_count

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.filter_url = reverse('topic:filter')
        self.full_url = reverse('topic:full', args=[1])
        self.new_post_url = reverse('topic:new_post')
        self.new_category_url = reverse('topic:new_category')

    def test_filter_GET_nocatid(self):
        response = self.client.get(self.filter_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('topic/filter.html')
    
    def test_full_GET(self):
        response = self.client.get(self.full_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('topic/full.html')
        