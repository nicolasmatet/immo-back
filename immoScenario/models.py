from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class ImmoScenario(models.Model):
    title = models.TextField(default='Untitled')
    created_date = models.DateField(default=datetime.now)
    achat_valeur_bien = models.FloatField(default=0)
    achat_notaire_taux = models.FloatField(default=0)
    achat_apport_personnel = models.FloatField(default=0)
    achat_emprunt_capital = models.FloatField(default=0)
    achat_emprunt_taux = models.FloatField(default=0)

    loca_montant_loyer = models.FloatField(default=0)
    loca_charges = models.FloatField(default=0)

    compta_amortissement_duree = models.FloatField(default=0)
