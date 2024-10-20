from django.urls import path

from . import views

urlpatterns = [
    path(
        "insert_new", views.insert_new, name="insert_new"
    ),  # inserimento nuovo paziente
    path(
        "patient_search", views.patient_search, name="patient_search"
    ),  # ricerca paziente
    path("edit_data/<int:pk>/", views.edit_data, name="edit_data"),  # Modifica dati
]
