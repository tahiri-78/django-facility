from django.db import models
from user.models import user
from operation.models import operation

class saisie(models.Model):
    id_saisie=models.AutoField(primary_key=True)
    Participation_id=models.CharField(max_length=100)
    ancien_idPlateforme=models.CharField(max_length=100)
    num_conso=models.CharField(max_length=100)
    op_name=models.CharField(max_length=100)
    civilite=models.CharField(max_length=10)
    raison_social=models.CharField(max_length=100)
    Nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse1=models.CharField(max_length=100)
    adresse2=models.CharField(max_length=100)
    adresse3=models.CharField(max_length=100)
    adresse4=models.CharField(max_length=100)
    CodePostal=models.CharField(max_length=10)
    ville=models.CharField(max_length=100)
    pays=models.CharField(max_length=100)
    langue=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Tel=models.CharField(max_length=100)
    nombre_pneus_base=models.CharField(max_length=10)
    diametre_pneus_base=models.CharField(max_length=10)
    num_pdv_base=models.CharField(max_length=100)
    date_achat_base=models.CharField(max_length=100)
    optin_base=models.CharField(max_length=10)
    optin_pdv_base=models.CharField(max_length=10)
    optin_auto_base=models.CharField(max_length=10)
    date_participation_base=models.CharField(max_length=100)
    type_pneus_base=models.CharField(max_length=100)
    idDotation_base=models.CharField(max_length=100)
    Montant_base=models.CharField(max_length=100)
    TypeBenefice_base=models.CharField(max_length=100)
    TAS=models.CharField(max_length=100)
    date_saisie=models.DateTimeField(auto_now_add=True)
    date_modification=models.DateTimeField(auto_now=True)
    Date_Select=models.CharField(max_length=100)
    Etat_select=models.CharField(max_length=100)
    Date_Cloture=models.DateTimeField(auto_now=True)
    Commentaire=models.CharField(max_length=100)
    etat=models.CharField(max_length=100)
    user = models.OneToOneField(
        user,
        on_delete=models.DO_NOTHING
    )
    operation = models.ForeignKey(operation, on_delete=models.DO_NOTHING)
    


