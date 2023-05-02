from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import index, signup

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup)
    