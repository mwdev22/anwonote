from django.test import TestCase
from topic.factories import CategoryFactory, TopicFactory
from topic.models import Topic

 

class CategoryTestCase(TestCase):
    def setUp(self):
        self.categories = CategoryFactory.create_batch(10)
    def test_category_creation(self):
        for cat in self.categories:
            cat.save()
            self.assertIsNotNone(cat.id)

class TopicTestCase(TestCase):
    def setUp(self):
        self.topics = TopicFactory.create_batch(10)
    def test_topic_creation(self):
        for topic in self.topics:
            topic.save()
            self.assertIsNotNone(topic.id)
    def test_status_test(self):
        for topic in self.topics:
        #   sprawdzanie poprawności wybranego statusu (głównie na potrzeby testu, na stronie i tak są jako choicefield)
            self.assertIn(topic.status,  [choice[0] for choice in Topic.STATUS_CHOICES])
