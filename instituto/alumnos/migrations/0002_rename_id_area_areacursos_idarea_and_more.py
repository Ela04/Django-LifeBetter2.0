# Generated by Django 4.2.1 on 2023-06-09 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areacursos',
            old_name='id_Area',
            new_name='idArea',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='id_Area',
            new_name='idArea',
        ),
    ]
