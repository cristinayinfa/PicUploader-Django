from django.db import models

# Create your models here.
class Photo(models.Model):
	name = models.CharField(max_length=120) 
	photo = models.ImageField(upload_to='photos/')
