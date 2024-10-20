from django.forms import ModelForm, DateInput
from .models import Patient, PatientSearchAnagraphic


# Classe per abilitare l'input del tipo data
class DateInput(DateInput):
    input_type = "date"


# Classe per la creazione del form
class Anagraphic(ModelForm):
    class Meta:
        model = Patient
        fields = [
            "anagraphicSurname",
            "anagraphicName",
            "anagraphicBirthdate",
            "anagraphicGender",
        ]
        widgets = {
            "anagraphicBirthdate": DateInput(),
        }


class Intraoperative(ModelForm):
    class Meta:
        model = Patient
        fields = ["intraoperativaSide", "intraoperativaDate", "intraoperativaSurgeon"]

        widgets = {
            "intraoperativaDate": DateInput(),
        }


# Classe per la ricerca
class PatientSearchForm(ModelForm):
    class Meta:
        model = PatientSearchAnagraphic
        fields = "__all__"
        widgets = {
            "birthdate": DateInput(),
        }
