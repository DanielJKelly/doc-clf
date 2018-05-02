from django.db import models
from django.utils import timezone

# Create your models here.

class Doc(models.Model):
    batch_name = models.CharField(max_length=50)
    predicted_class = models.IntegerField(default=0)
    actual_class = models.IntegerField(default=0)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    original_file_name = models.CharField(max_length=200)
    file_line_num = models.IntegerField()