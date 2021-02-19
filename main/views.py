from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def gestion(request):
    return render(request, 'main/gestion.html')


def contact(request):
    return render(request, 'main/contact.html')

