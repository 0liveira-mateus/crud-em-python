from django.db import models

class carros(models.Model):
    Modelo = models.CharField(max_length=150)
    Marca = models.CharField(max_length=100)
    Ano = models.IntegerField()