from django.db import models
from user.models import user
from operation.models import operation

class Lots(models.Model):
    nom_lot=models.CharField(max_length=10)
    qte_declare=models.IntegerField(max_length=10)
    qte_saisie=models.IntegerField(max_length=10)
    active=models.IntegerField(max_length=10)
    annee=models.DateTimeField(auto_now_add= True)
    user=models.ManyToManyField(user)
    operation = models.ForeignKey(operation, on_delete=models.DO_NOTHING)



    def __str__(self):
        return self.nom_lot



    