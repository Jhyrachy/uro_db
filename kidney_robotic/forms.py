from django.forms import ModelForm, DateInput
from .models import Robotics_Kidneys, PatientSearchAnagraphic

# Libreria datepicker bootstrap 5
from bootstrap_datepicker_plus.widgets import DatePickerInput


# Classe per la creazione del form
class Anagraphic(ModelForm):
    class Meta:
        model = Robotics_Kidneys
        fields = [
            "anagraphicSurname",
            "anagraphicName",
            "anagraphicBirthdate",
            "anagraphicGender",
        ]
        widgets = {"anagraphicBirthdate": DateInput(attrs={"type": "date"})}


class Intraoperative(ModelForm):
    class Meta:
        model = Robotics_Kidneys
        fields = ["intraoperativaSide", "intraoperativaDate", "intraoperativaSurgeon"]

        # widgets = {"intraoperativaDate": DateInput(attrs={"type": "date"})}
        widgets = {
            "intraoperativaDate": DatePickerInput(options={"format": "DD/MM/YYYY"})
        }


# Classe per la ricerca
class PatientSearchForm(ModelForm):
    class Meta:
        model = PatientSearchAnagraphic
        fields = "__all__"
        widgets = {"birthdate": DateInput(attrs={"type": "date"})}