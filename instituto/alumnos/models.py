from django.db import models
# Create your models here.

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True)  # Campo de clave primaria autoincremental para 'Genero'
    genero     = models.CharField(max_length=20, blank=False, null=False)  # Campo de texto para el nombre del género

    def __str__(self):
        return str(self.genero)  # Representación en cadena del modelo 'Genero'


class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)  # Campo de clave primaria para el RUT del alumno
    nombre           = models.CharField(max_length=20)  # Campo de texto para el nombre del alumno
    apellido_paterno = models.CharField(max_length=20)  # Campo de texto para el apellido paterno
    apellido_materno = models.CharField(max_length=20)  # Campo de texto para el apellido materno
    fecha_nacimiento = models.DateField(blank=False, null=False)  # Campo de fecha para la fecha de nacimiento
    id_genero        = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')  # Clave foránea a 'Genero'
    telefono         = models.CharField(max_length=45)  # Campo de texto para el teléfono
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)  # Campo de email único
    direccion        = models.CharField(max_length=50, blank=True, null=True)  # Campo de texto para la dirección
    activo           = models.IntegerField()  # Campo entero para indicar si el alumno está activo

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)  # Representación en cadena del modelo 'Alumno'

    class Meta:
        ordering = ['rut']  # Ordena por 'rut' de forma predeterminada


# Tarea en Clases
class AreaCursos(models.Model):
    id_Area = models.AutoField(db_column='id_Area', primary_key=True, default=1)  # Campo de clave primaria autoincremental para 'AreaCursos'
    Descripcion = models.CharField(max_length=30, blank=False, null=False)  # Campo de texto para la descripción del área

    def __str__(self):
        return str(self.Descripcion)  # Representación en cadena del modelo 'AreaCursos'


class ModalCursos(models.Model):
    id_Modal        = models.AutoField(db_column='idModal', primary_key=True)  # Campo de clave primaria autoincremental para 'ModalCursos'
    Descripcion     = models.CharField(max_length=30, blank=True, null=True)  # Campo de texto para la descripción de la modalidad

    def __str__(self):
        return str(self.Descripcion)  # Representación en cadena del modelo 'ModalCursos'


class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    sence = models.CharField(max_length=10)
    fecha_creacion = models.DateField(blank=False, null=False)
    id_Area = models.ForeignKey('AreaCursos', on_delete=models.CASCADE, db_column='id_Area') 
    modalidad = models.CharField(max_length=30, blank=True, null=True)
    objetivo = models.CharField(max_length=200, blank=True, null=True)
    horas = models.IntegerField()
    activo = models.IntegerField()
    img = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return str(self.nombre)  # Representación en cadena del modelo 'Cursos'

    class Meta:
        ordering = ['nombre']  # Ordena por 'nombre' de forma predeterminada
