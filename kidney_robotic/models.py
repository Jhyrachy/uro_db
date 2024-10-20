from django.db import models

# Strutture per le selezioni
GENDER = [
    ("F", "Female"),
    ("M", "Male"),
]
SIDE = [
    ("R", "Right"),
    ("L", "Left"),
    ("B", "Bilateral"),
]
SURGEON = [
    ("BE", "Brunocilla"),
    ("SR", "Schiavina"),
    ("BL", "Bianchi"),
    ("CF", "Chessa"),
]


# Create your models here.
class Patient(models.Model):

    # Scheda anagrafica
    anagraphicId = models.IntegerField(primary_key=True)
    anagraphicSurname = models.CharField(max_length=50)
    anagraphicName = models.CharField(max_length=50)
    anagraphicBirthdate = models.DateField()
    anagraphicGender = models.CharField(max_length=10, choices=GENDER)

    # Scheda intraoperatoria
    intraoperativaSide = models.CharField(max_length=1, choices=SIDE)
    intraoperativaDate = models.DateField()
    intraoperativaSurgeon = models.CharField(max_length=20, choices=SURGEON)
