from django.test import TestCase
from humain.models import Famille
# Create your tests here.


class FamilleTestCase(TestCase):
    def test_creationsimple(self):
        Famille.objects.create(
            nom="Hornor",
            composition=True,
            cpas_particulier=False,
            pharmacie=False,
            bus=True,
            bte=False
        )

    def test_creationcomplete(self):
        Famille.objects.create(
            nom="Danield",
            nbrAdulte=2,
            nbrEnfant=4,
            nbrColis=3,
            dateDernierColis="2021-05-15 12:45",
            composition=True,
            date_cpas="2021-05-15 12:45",
            cpas_particulier=False,
            pharmacie=False,
            bus=True,
            bte=False
        )