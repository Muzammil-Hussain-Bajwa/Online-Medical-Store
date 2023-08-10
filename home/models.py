from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=222)
    email= models.CharField(max_length=222)
    phone= models.CharField(max_length=222)
    desc= models.TextField(max_length=222)