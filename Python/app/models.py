from django.db import models

# Create your models here.

class carros(models.Model):
    Modelo = models.CharField(max_length=30)
    Marca = models.CharField(max_length=30)
    Ano = models.IntegerField()