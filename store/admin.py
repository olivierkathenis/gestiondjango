from django.contrib import admin
from .models import Fournisseur, TypeProduit, Produit, Stock


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'rue', 'numero', 'ville', 'pays')
    search_fields = ['nom']


class TypeProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', "unite_mesure")
    search_fields = ['nom']


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'datesortie', 'dateconservation', 'quantite', 'type')
    search_fields = ['nom']


class StockAdmin(admin.ModelAdmin):
    list_display = ('nom_produit', 'nombreStock', 'nombreVendu', 'nombreSupprime')


admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(TypeProduit, TypeProduitAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Stock, StockAdmin)