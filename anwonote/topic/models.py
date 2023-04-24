from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=35)
    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        verbose_name_plural='Categories'
    # elementy tabeli zwracają swoją nazwe 
    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
# 1 element tupli w kodzie html, 2 element widoczny w formularzu
    STATUS_CHOICES = (
        ('tylko dla mnie', 'Tylko dla mnie'),
        ('dla wszystkich', 'Dla wszystkich'),
        ('dla zalogowanych', 'Dla zalogowanych')
    )
    category = models.ForeignKey(Category,related_name='topics', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='Tylko dla mnie')

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("-created_at",)

