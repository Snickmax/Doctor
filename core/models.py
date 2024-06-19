from django.db import models
from django.contrib.auth.models import AbstractUser
    
class usuarios(AbstractUser):
    email = models.EmailField(unique=True)
    last_name2 = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.username
    
class paciente(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    rut = models.CharField(max_length=12, primary_key=True, verbose_name="RUT")
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido paterno")
    last_name2 = models.CharField(max_length=50, verbose_name="Apellido materno")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sexo")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(verbose_name="Fecha de Nacimiento")
    phone_number = models.CharField(max_length=15, verbose_name="Número de Celular")
    address = models.CharField(max_length=100, verbose_name="domicilio")
    city = models.CharField(max_length=50, verbose_name="localidad")
    state = models.CharField(max_length=50, verbose_name="provincia")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.rut}"

class cita(models.Model):
    patient = models.ForeignKey(paciente, on_delete=models.CASCADE, related_name='appointments', verbose_name="Paciente")
    date = models.DateField(verbose_name="Fecha")
    time = models.TimeField(verbose_name="Hora")
    reason = models.TextField(verbose_name="Motivo")

    def __str__(self):
        return f"Appointment for {self.person.first_name} {self.person.last_name} on {self.date} at {self.time}"