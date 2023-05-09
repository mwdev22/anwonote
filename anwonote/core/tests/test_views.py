from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
