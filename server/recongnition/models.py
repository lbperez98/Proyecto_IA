from django.db import models

# Create your models here.


class PlantaModel(models.Model):
    nombre = models.CharField(max_length = 100)
    nombreCientifico = models.CharField(max_length =200)
    descripcion = models.CharField(max_length = 500)