# Generated by Django 4.2.16 on 2024-10-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientSearchAnagraphic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
            ],
        ),
        migrations.CreateModel(
            name='Robotics_Kidneys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anagraphicSurname', models.CharField(help_text='<i>(Cognome del paziente)</i><br><br>', max_length=50, verbose_name='Cognome')),
                ('anagraphicName', models.CharField(help_text='<i>(Nome del paziente)</i><br><br>', max_length=50, verbose_name='Nome')),
                ('anagraphicBirthdate', models.DateField(help_text='<br><br>', verbose_name='Data di nascita')),
                ('anagraphicGender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], help_text='<br><br>', max_length=10, verbose_name='Genere')),
                ('intraoperativaSide', models.CharField(choices=[('R', 'Right'), ('L', 'Left'), ('B', 'Bilateral')], max_length=1, null=True)),
                ('intraoperativaDate', models.DateField(null=True)),
                ('intraoperativaSurgeon', models.CharField(choices=[('BE', 'Brunocilla'), ('SR', 'Schiavina'), ('BL', 'Bianchi'), ('CF', 'Chessa')], max_length=20, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='robotics_kidneys',
            constraint=models.UniqueConstraint(fields=('anagraphicSurname', 'anagraphicName', 'anagraphicBirthdate'), name='unique_patient'),
        ),
    ]
