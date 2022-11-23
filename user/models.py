from django.db import models


class user(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    matricule=models.CharField(max_length=20)
    date_creation=models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.matricule+ " : "+ self.nom

