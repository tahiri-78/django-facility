Table (application) :

 1- Saisie = comporte la saisie des enregistrement réçu
    - {entete operation }
    - etat 
    - date_creation
    - date_modification
    - fichier_origine
    



 2 - Lot = un numéro affecté a un ensemble de enregistrement selon la date de réception 
     - nom_lot
     - qte_declare
     - qte_saisie
     - active
     - annee
     - semaine

3 - Operation  = ensembles de operation qui permette de saisie ces enregistrement c à d  un cahier de charge permet de mettre en place les champs à saisir
     -nom_operation
     -objectif
     -theme
     -date_creation
     -date_modification
     -client
     -entete

 4 - User = les oper qui effecture la saisie des ces enregistrement 
     -nom
     -prenom
     -matricule
     -date_creation

5 - Fichier = le fichier des enregistrement à traiter 
    -nom_fichier
    -date_reception
    -type_fichier
    -client
------------------------------------------------------------------------------------------------------------------------------------------------------
    Apps demandé :
    1 - Saisie
    2 - lot
    3 - Operation
    4 - User
    5 - Fichier
    6 - Homme
    7 - Login

