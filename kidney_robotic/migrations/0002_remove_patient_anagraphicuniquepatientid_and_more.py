# Generated by Django 5.1.2 on 2024-10-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidney_robotic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='anagraphicUniquePatientID',
        ),
        migrations.AddConstraint(
            model_name='patient',
            constraint=models.UniqueConstraint(fields=('anagraphicSurname', 'anagraphicName', 'anagraphicBirthdate'), name='unique_patient'),
        ),
    ]
