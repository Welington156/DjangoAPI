from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=120)
    material = models.CharField(max_length=120)
    classify = models.CharField(max_length=120)
    preco = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)