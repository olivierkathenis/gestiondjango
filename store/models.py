from django.db import models


class Fournisseur(models.Model):
    nom = models.CharField(max_length=200)
    rue = models.TextField(null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    ville = models.CharField(max_length=250,null=True, blank=True)
    codepostal = models.IntegerField(null=True, blank=True)
    pays = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return self.nom


class TypeProduit(models.Model):
    nom = models.CharField(max_length=200)
    unite_mesure = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=250)
    prix = models.FloatField()
    dateentree = models.DateTimeField(auto_now_add=True, blank=True)
    datesortie = models.DateTimeField(null=True, blank=True)
    dateconservation = models.DateTimeField()
    quantite = models.IntegerField(null=True)
    poids = models.CharField(max_length=100, null=True)
    type = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Stock(models.Model):
    nom_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    nombreStock = models.IntegerField(null=True)
    nombreVendu = models.IntegerField(null=True)
    nombreSupprime = models.IntegerField(null=True)