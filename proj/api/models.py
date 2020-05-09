from django.db import models

class Image(models.Model):
	image = models.ImageField(upload_to ='uploads/')
	title = models.CharField(max_length=128)