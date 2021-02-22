from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Fournisseur, TypeProduit, Produit, Stock
from .forms import CreerProduitForm
from .forms import ModifierProduitForm
from .forms import CreerTypeProduit
from .forms import CreerFournisseur


def index(request):
    produits = Produit.objects.all().order_by('dateconservation')
    stock = Stock.objects.all()
    return render(request, 'store/index.html', {
        'produits': produits, 'stock': stock
    })


def retirer(request, produit_id):
    try:
        id = int(produit_id)
        produits = Produit.objects.all().order_by('dateconservation')
        produit = Produit.objects.get(pk=id)
        produit.quantite = int(produit.quantite - 1)
        produit.save()
        return render(request, 'store/index.html', {'produits': produits})
    except Produit.DoesNotExist:
        raise Http404("Le produit n'existe pas")


def creer(request):
    form = CreerProduitForm()
    if request.method == 'POST':
        form = CreerProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store:index'))
    else:
        form = CreerProduitForm()
    return render(request, 'store/creer.html', {'form': form})


def mettre_jour(request, produit_id):
    id = int(produit_id)
    context = {}
    obj = get_object_or_404(Produit, id=id)
    form = ModifierProduitForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        produits = Produit.objects.all()
        return render(request, 'store/index.html', {'produits': produits})
    context["form"] = form
    return render(request, "store/mettre_jour.html", context)


def creer_fournisseur(request):
    form = CreerFournisseur()
    if request.method == 'POST':
        form = CreerFournisseur(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store:index'))
    else:
        form = CreerFournisseur()
    return render(request, 'store/creation_fournisseur.html', {'form': form})


def creer_typeproduit(request):
    form = CreerTypeProduit()
    if request.method == 'POST':
        form = CreerTypeProduit(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store:index'))
    else:
        form = CreerTypeProduit()
    return render(request, 'store/creation_typeproduit.html', {'form': form})

