from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Anagraphic, PatientSearchForm, Intraoperative
from .models import Patient, PatientSearchAnagraphic


# Create your views here.
def insert_new(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Anagraphic(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            # Se modifica form.save(commit=False) resituisce un oggetto modello che puoi modificare e poi model.save() per salvare nel db
            return HttpResponseRedirect("/kidney_robotic/insert_new")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Anagraphic()

    return render(
        request, "master.html", {"form": form, "page_title": "New patient anagraphic"}
    )


# Search view
def patient_search(request):
    pk_patient = None
    error = None

    if request.method == "POST":
        form = PatientSearchForm(request.POST)
        if form.is_valid():
            try:
                persona = Patient.objects.get(
                    anagraphicName=form.cleaned_data["name"],
                    anagraphicSurname=form.cleaned_data["surname"],
                    anagraphicBirthdate=form.cleaned_data["birthdate"],
                )  # Importante cercare nella tabella giusta
                pk_patient = persona.pk
                return redirect("edit_data", pk=persona.pk)
            except Patient.DoesNotExist:
                error = "Patient not found in the database"

    else:
        form = PatientSearchForm()

    return render(
        request,
        "search.html",
        {"form": form, "pk_persona": pk_patient, "errore": error},
    )


# Edit data using a primary key
def edit_data(request, pk):
    # Recupera l'oggetto usando la PK passata dal form di ricerca
    instance = get_object_or_404(Patient, pk=pk)

    persona = instance.objects.get(anagraphicName=pk)

    if request.method == "POST":
        form = PatientSearchForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  # Salva le modifiche
            return redirect("success_url")  # Reindirizza a una pagina di successo
    else:
        form = PatientSearchForm(instance=instance)

    return render(
        request,
        "edit_data.html",
        {
            "form": form,
            "page_title": "Intraoperative data",
            "name": persona.anagraphicName,
            "surname": persona.anagraphicSurname,
            "birthdate": persona.anagraphicBirthdate,
        },
    )
