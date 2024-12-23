from django.db import models

# Create your models here.
class Box(models.Model):
    name = models.CharField(max_length=100)  # Nom ou numéro de la box
    capacity = models.IntegerField()         # Capacité de la box
    location = models.CharField(max_length=200)  # Localisation

    def __str__(self):
        return self.name

class Reservations(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Utilisateur qui réserve
    box = models.ForeignKey(Box, on_delete=models.CASCADE)           # Box réservée
    start_time = models.DateTimeField()                              # Début de la réservation
    end_time = models.DateTimeField()                                # Fin de la réservation
    code = models.CharField(max_length=10, unique=True)              # Code unique pour vérifier

    def __str__(self):
        return f"Réservation {self.code} pour {self.box.name}"

