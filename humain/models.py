from datetime import datetime
from django.db import models


class Famille(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    nbrAdulte = models.IntegerField(default=1)
    nbrEnfant = models.IntegerField(default=0)
    nbrColis = models.IntegerField(default=0)
    dateDernierColis = models.DateTimeField(null=True, blank=True)
    composition = models.BooleanField()
    date_cpas = models.DateTimeField(null=True, blank=True)
    cpas_particulier = models.BooleanField()
    pharmacie = models.BooleanField()
    bus = models.BooleanField()
    bte = models.BooleanField()

    def __str__(self):
        return self.nom

