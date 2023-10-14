from django.db import models
from django.utils import timezone
# Create your models here.
'''
- felids , options
- validation
- html widget

'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default=timezone.now())
    draft = models.BooleanField(default=True)
