import datetime

from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CreationFamilleForm
from .forms import ModifFamilleForm
from .models import Famille


def index(request):
    famille = Famille.objects.all()
    return render(request, 'humain/index.html', {'famille': famille})


def colis(request):
    famille = Famille.objects.all()
    return render(request, 'humain/colis.html', {'famille': famille})


def gestion(request, famille_id):
    id = int(famille_id)
    famille = Famille.objects.filter(pk=id)
    return render(request, 'humain/gestion.html', {'famille': famille})


def creer(request):
    form = CreationFamilleForm()
    if request.method == 'POST':
        form = CreationFamilleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('humain:index'))
    else:
        form = CreationFamilleForm()
    return render(request, 'humain/creer.html', {'form': form})


def mettre_jour(request, famille_id):
    id = int(famille_id)
    context = {}
    obj = get_object_or_404(Famille, id=id)
    form = ModifFamilleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        familles = Famille.objects.all()
        return render(request, 'humain/index.html', {'famille': familles})
    context["form"] = form
    return render(request, "humain/mettre_jour.html", context)


def ajouter_colis(request, famille_id):
    try:
        id = int(famille_id)
        familles = Famille.objects.all()
        famille = Famille.objects.get(pk=id)
        famille.dateDernierColis = datetime.datetime.now()
        famille.nbrColis += 1
        famille.save()
        return render(request, 'humain/colis.html', {'famille': familles})
    except Famille.DoesNotExist:
        raise Http404("Une erreur est survenue")