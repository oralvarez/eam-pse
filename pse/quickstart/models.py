from django.db import models

# Create your models here.
class Nota(models.Model):
	nombre = models.CharField(max_length=100)
	detalle = models.CharField(max_length=500)

