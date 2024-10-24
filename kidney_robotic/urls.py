from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path(
        "insert_new", login_required(views.insert_new), name="insert_new"
    ),  # inserimento nuovo paziente
    path(
        "patient_search", views.patient_search, name="patient_search"
    ),  # ricerca paziente
    path("edit_patient/<int:pk>/", views.edit_data, name="edit_data"),  # Modifica dati
    path(
        "new_patient/<str:database>",
        views.insert_new_dynamic,
        name="insert_new_dynamic",
    ),
]
