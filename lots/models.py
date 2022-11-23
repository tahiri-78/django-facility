from django.db import models

class Lots(models.Model):
    nom_lot=models.CharField(max_length=10)
    qte_declare=models.IntegerField(max_length=10)
    qte_saisie=models.IntegerField(max_length=10)
    active=models.IntegerField(max_length=2)
    annee=models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.nom_lot



    