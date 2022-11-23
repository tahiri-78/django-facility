from django.db import models


class operation(models.Model):
    id_op=models.AutoField(primary_key=True)
    nom_operation=models.CharField(max_length=10)
    object=models.IntegerField(max_length=10)
    theme=models.CharField(max_length=100)
    date_creation=models.DateTimeField(auto_now_add=True)
    date_modification=models.DateTimeField(auto_now=True)
    client_op=models.CharField(max_length=20)
    entete=models.CharField(max_length=900)
    



