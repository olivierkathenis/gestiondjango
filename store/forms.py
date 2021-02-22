from django.forms import ModelForm, NumberInput, DateInput
from .models import Produit, TypeProduit, Fournisseur


class CreerProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = [
            'nom',
            'prix',
            'dateconservation',
            'quantite',
            'poids',
            'type',
            'fournisseur'
        ]
        widgets = {
            'dateconservation': DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Choisissez une date',
                       'type': 'date'
                       }),
        }


class ModifierProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = [
            'nom',
            'prix',
            'dateconservation',
            'quantite',
            'poids',
            'type',
            'fournisseur'
        ]
        widgets = {
            'dateconservation': DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Choisissez une date',
                       'type': 'date'
                       }),
        }


class CreerTypeProduit(ModelForm):
    class Meta:
        model = TypeProduit
        fields = [
            'nom'
        ]


class CreerFournisseur(ModelForm):
    class Meta:
        model = Fournisseur
        fields = [
            'nom',
            'rue',
            'numero',
            'ville',
            'codepostal',
            'pays'
        ]