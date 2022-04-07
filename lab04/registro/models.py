from django.db import models

# Create your models here.
class Region(models.Model):
    name_region = models.CharField(max_length=100)
    
class Candidato(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    candidatura = models.CharField(max_length=60)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ideologia = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    