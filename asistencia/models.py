from django.core.validators import RegexValidator
from django.db import models


class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento_identidad = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[0-9A-Za-z]+$',
                message='El documento de identidad solo puede contener caracteres alfanuméricos.',
            ),
        ],
    )
    correo_electronico = models.EmailField()
    fecha_asistencia = models.DateField()
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    presente = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha_asistencia}"
