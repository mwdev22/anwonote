from django.test import SimpleTestCase
from django.urls import reverse, resolve
import topic.views as views
from random import randint
from topic.models import Topic, Category

topics_count = Topic.objects.all().count()
category_count = Category.objects.all().count()

class TestUrls(SimpleTestCase):
    
    def test_filter_url(self):
        url = reverse('topic:filter')
        self.assertEquals(resolve(url).func, views.filter)

# adresy dodające elementy do bazy danych
    def test_new_post_url(self):
        url = reverse('topic:new_post')
        self.assertEquals(resolve(url).func, views.new_post)
    
    def test_new_category_url(self):
        url = reverse('topic:new_category')
        self.assertEquals(resolve(url).func, views.new_category)

    def test_delete_category(self):
        url = reverse('topic:delete_category')
        self.assertAlmostEquals(resolve(url).func, views.delete_category)
# adresy wymagające pk
    def test_full_url(self):
# testuje adres dla dowolnego postu, pk nie może być większy niż ilość postów 
        url = reverse('topic:full', args=[randint(1, topics_count)])
        self.assertEquals(resolve(url).func, views.full)
    def test_delete_post(self):
        url = reverse('topic:delete_post', args=[randint(1, topics_count)])
        self.assertEquals(resolve(url).func, views.delete_post)
    

