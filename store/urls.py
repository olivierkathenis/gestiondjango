from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = "store"


urlpatterns = [
    path('', login_required(views.index), name="index"),
    path('<int:produit_id>', login_required(views.retirer), name="retirer"),
    path('creation_produit', login_required(views.creer), name="creer"),
    path('creation_fournisseur', login_required(views.creer_fournisseur), name='fournisseur'),
    path('creation_typeproduit', login_required(views.creer_typeproduit), name='typeproduit'),
    path('<int:produit_id>/mettre_jour', login_required(views.mettre_jour), name="mettre_jour")
]

