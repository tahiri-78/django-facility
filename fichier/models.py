from django.db import models

# Create your models here.

class Fichier(models.Model):
    nom_fichier=models.CharField(max_length=100)
    date_creation=models.DateTimeField(auto_now_add=True)
    date_modification=models.DateTimeField(auto_now=True)
    type_fichier=models.CharField(max_length=50)
    client=models.CharField(max_length=50)

    
