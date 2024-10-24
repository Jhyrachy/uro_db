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


# Campi utili:
## verbose_name: sostituisce il nome del campo
## help_text: aggiunge una descrizione al campo


# Create your models here.
class Robotics_Kidneys(models.Model):
    class Meta:
        #Controllo sull'unicità del paziente
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "anagraphicSurname",
                    "anagraphicName",
                    "anagraphicBirthdate",
                ],
                name="unique_patient",
            )
        ]

    # Scheda anagrafica
    anagraphicSurname = models.CharField(
        max_length=50,
        verbose_name="Cognome",
        help_text="<i>(Cognome del paziente)</i><br><br>",
    )
    anagraphicName = models.CharField(
        max_length=50,
        verbose_name="Nome",
        help_text="<i>(Nome del paziente)</i><br><br>",
    )
    anagraphicBirthdate = models.DateField(
        verbose_name="Data di nascita", help_text="<br><br>"
    )
    anagraphicGender = models.CharField(
        max_length=10, choices=GENDER, verbose_name="Genere", help_text="<br><br>"
    )

    # Scheda intraoperatoria
    intraoperativaSide = models.CharField(max_length=1, choices=SIDE, null=True)
    intraoperativaDate = models.DateField(null=True)
    intraoperativaSurgeon = models.CharField(max_length=20, choices=SURGEON, null=True)


# Class for the search
class PatientSearchAnagraphic(models.Model):
    surname = models.CharField(verbose_name="Surname", max_length=100)
    name = models.CharField(verbose_name="Name", max_length=100)
    birthdate = models.DateField(verbose_name="Birthdate")
