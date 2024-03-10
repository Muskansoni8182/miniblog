from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=150)
    upload=models.ImageField(upload_to='uploads/')
    desc=models.TextField()
