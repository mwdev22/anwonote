from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json
from core.forms import UserCreationForm

import core.views as views
from topic.models import Category, Topic

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.signup_url = reverse('signup')

    
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
    
    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/signup.html')

    def test_signup_POST_new_user(self):
        data = {
            'username':'testuser',
            'email':'testmail@example.com',
            'password1':'hasłotest',
            'password2':'hasłotest'
        }
    
        response = self.client.post(self.signup_url, data)

        # sprawdzanie przekierowania
        self.assertEquals(response.status_code, 302)

        # sprawdzanie, czy użytkownik został utworzony po wysłaniu formularza
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testmail@example.com')