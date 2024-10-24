from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Anagraphic, PatientSearchForm, Intraoperative
from .models import Robotics_Kidneys, PatientSearchAnagraphic
from django.db import IntegrityError

# Libreria per la modelformfactory
from django.forms import modelform_factory


# Create your views here.
def insert_new(request):
    error = None
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Anagraphic(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                lowercasing = form.save(commit=False)
                lowercasing.anagraphicSurname = lowercasing.anagraphicSurname.lower()
                lowercasing.anagraphicName = lowercasing.anagraphicName.lower()
                lowercasing.save()
                # Se modifica form.save(commit=False) resituisce un oggetto modello che puoi modificare e poi model.save() per salvare nel db
                return HttpResponseRedirect("/kidney_robotic/insert_new")
            except IntegrityError as e:
                if "unique constraint" in e.args[0]:  # or e.args[0] from Django 1.10
                    error = "A patient with this name and surname already exists."

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Anagraphic()

    return render(
        request,
        "forms/insert_patient.html",
        {
            "form": form,
            "page_title": "New patient anagraphic",
            "errore": error,
        },
    )


# Search view
def patient_search(request):
    pk_patient = None
    error = None

    if request.method == "POST":
        form = PatientSearchForm(request.POST)
        if form.is_valid():
            try:
                persona = Robotics_Kidneys.objects.get(
                    anagraphicName=form.cleaned_data["name"].lower(),
                    anagraphicSurname=form.cleaned_data["surname"].lower(),
                    anagraphicBirthdate=form.cleaned_data["birthdate"],
                )  # Importante cercare nella tabella giusta
                pk_patient = persona.pk
                print(pk_patient)
                return redirect("edit_data", pk=persona.pk)
            except Robotics_Kidneys.DoesNotExist:
                error = "Patient not found in the database"

    else:
        form = PatientSearchForm()

    return render(
        request,
        "forms/search_patient.html",
        {"form": form, "pk_persona": pk_patient, "errore": error},
    )


# Edit data using a primary key
def edit_data(request, pk):
    # Recupera l'oggetto usando la PK passata dal form di ricerca
    print(pk)
    persona = get_object_or_404(Robotics_Kidneys, pk=pk)

    if request.method == "POST":
        form = Intraoperative(request.POST, instance=persona)
        if form.is_valid():
            form.save()  # Salva le modifiche
            return redirect("success_url")  # Reindirizza a una pagina di successo
    else:
        form = Intraoperative(instance=persona)

    return render(
        request,
        "forms/edit_patient.html",
        {
            "form": form,
            "page_title": "Intraoperative data",
            "name": persona.anagraphicName,
            "surname": persona.anagraphicSurname,
            "birthdate": persona.anagraphicBirthdate,
            "id": persona.pk,
        },
    )


# TEST CLASS
def insert_new_dynamic(request, database):
    error = None
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = database(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                lowercasing = form.save(commit=False)
                lowercasing.anagraphicSurname = lowercasing.anagraphicSurname.lower()
                lowercasing.anagraphicName = lowercasing.anagraphicName.lower()
                lowercasing.save()
                # Se modifica form.save(commit=False) resituisce un oggetto modello che puoi modificare e poi model.save() per salvare nel db
                return HttpResponseRedirect("/kidney_robotic/insert_new")
            except IntegrityError as e:
                if "unique constraint" in e.args[0]:  # or e.args[0] from Django 1.10
                    error = "A patient with this name and surname already exists."

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Anagraphic()

    return render(
        request,
        "forms/insert_patient.html",
        {
            "form": form,
            "page_title": "New patient anagraphic",
            "errore": error,
        },
    )
