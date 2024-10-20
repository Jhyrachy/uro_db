from django.forms import ModelForm
from .models import Patient


class Anagraphic(ModelForm):
    class Meta:
        model = Patient
        fields = [
            "anagraphicSurname",
            "anagraphicName",
            "anagraphicBirthdate",
            "anagraphicGender",
        ]


class Intraoperative(ModelForm):
    class Meta:
        model = Patient
        fields = ["intraoperativaSide", "intraoperativaDate", "intraoperativaSurgeon"]
