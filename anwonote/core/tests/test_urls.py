from django.test import SimpleTestCase
from django.urls import reverse, resolve
import core.views as views

class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, views.index)

    def test_signup_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, views.signup)

#   Testowanie url z class.as_view()

    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, views.Logowanie)
    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, views.Wylogowanie)