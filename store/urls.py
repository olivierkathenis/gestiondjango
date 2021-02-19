from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = "store"


urlpatterns = [
    path('', login_required(views.index), name="index"),
    path('<int:produit_id>', login_required(views.retirer), name="retirer"),
    path('creation_produit', login_required(views.creer), name="creer"),
    path('<int:produit_id>/mettre_jour', login_required(views.mettre_jour), name="mettre_jour")
]