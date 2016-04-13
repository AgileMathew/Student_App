from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=400)
    age = models.CharField(max_length=300)
    
    
                               
