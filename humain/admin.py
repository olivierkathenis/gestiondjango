from django.contrib import admin
from .models import Famille


class FamilleAdmin(admin.ModelAdmin):
    list_display = (
            'nom',
            'nbrAdulte',
            'nbrEnfant',
            'nbrColis',
            'dateDernierColis',
            'composition',
            'date_cpas',
            'cpas_particulier',
            'pharmacie',
            'bus',
            'bte')

    search_fields = ['nom']
    list_filter = ['composition', 'cpas_particulier', 'pharmacie', 'bus', 'bte']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nom"].label = "Nom de Famille:"
        form.base_fields["nbrAdulte"].label = "Nombre d'adultes:"
        form.base_fields["nbrEnfant"].label = "Nombre d'enfants:"
        form.base_fields["dateDernierColis"].label = "Date du dernier colis reçu:"
        form.base_fields["composition"].label = "Composition du ménage reçue ?"
        form.base_fields["date_cpas"].label = "Date de validité du CPAS:"
        form.base_fields["cpas_particulier"].label = "CPAS particulier ?"
        form.base_fields["pharmacie"].label = "Pharmacie ?"
        form.base_fields["bus"].label = "Bus ?"
        form.base_fields["bte"].label = "Bte ?"
        return form


admin.site.register(Famille, FamilleAdmin)
