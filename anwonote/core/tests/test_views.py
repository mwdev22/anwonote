from django.test import TestCase, RequestFactory
from core.views import index, signup
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator

class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')