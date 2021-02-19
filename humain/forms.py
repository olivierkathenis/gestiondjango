from django.forms import ModelForm, SelectDateWidget, NumberInput, DateInput
from .models import Famille


class ModifFamilleForm(ModelForm):
    class Meta:
        model = Famille
        fields = [
            'nom',
            'prenom',
            'nbrAdulte',
            'nbrEnfant',
            'nbrColis',
            'dateDernierColis',
            'composition',
            'date_cpas',
            'cpas_particulier',
            'pharmacie',
            'bus',
            'bte'
        ]
        widgets = {
            'dateDernierColis': DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                        'placeholder': 'Choisissez une date',
                        'type': 'date'
              }),
            'date_cpas': DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Choisissez une date',
                       'type': 'date'
                       }),
        }


class CreationFamilleForm(ModelForm):
    class Meta:
        model = Famille
        fields = [
            'nom',
            'prenom',
            'nbrAdulte',
            'nbrEnfant',
            'composition',
            'date_cpas',
            'cpas_particulier',
            'pharmacie',
            'bus',
            'bte'
        ]
        widgets = {
            'date_cpas': NumberInput(attrs={'type': 'date'}),
        }