from django.db import models

# Create your models here.

class Equip(models.Model):
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom
    
class Jugador(models.Model):
    nom_complet = models.CharField(max_length=100)
    data_naixement = models.DateField()
    direccio = models.CharField(max_length=255)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()
    equip = models.ForeignKey(Equip, on_delete=models.CASCADE)
    numero_licencia = models.CharField(max_length=20, unique=True)
    historial_medico = models.TextField()

    def __str__(self):
        return f"{self.nom_complet} - {self.equip.nom}"