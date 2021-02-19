from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = "humain"


urlpatterns = [
    path('', views.index, name='index'),

    path('gestion/<int:famille_id>', login_required(views.gestion), name='gestion'),
    path('colis', login_required(views.colis), name='colis'),
    path('ajouter_colis/<int:famille_id>', login_required(views.ajouter_colis), name='ajouter_colis'),
    path('creation_famille', login_required(views.creer), name="creer"),
    path('<int:famille_id>/mettre_jour', login_required(views.mettre_jour), name="mettre_jour")
]