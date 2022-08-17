from sqlite3 import Time
from django.db import models

# Create your models here.
class Task(models.Model):
    numeroplaca = models.CharField(max_length=100)
    horapartida = models.CharField(max_length=100)
    llegadahora = models.CharField(max_length=100)
    horaviaje = models.CharField(max_length=100)
    partida = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    costo = models.CharField(max_length=100)
