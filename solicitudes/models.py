from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models


class Solicitud(models.Model):
    """
    Modelo para gestionar solicitudes de los usuarios.
    Contiene información del solicitante y detalles de su solicitud.
    """

    TIPO_SOLICITUD_CHOICES = [
        ('académica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('técnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre_solicitante = models.CharField(
        max_length=150,
        help_text='Nombre completo del solicitante'
    )

    documento_identidad = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[0-9A-Za-z]+$',
                message='El documento de identidad solo puede contener caracteres alfanuméricos.',
            ),
        ],
        help_text='Documento de identidad (cedula, pasaporte, etc.)'
    )

    correo_electronico = models.EmailField(
        help_text='Correo electrónico para contacto'
    )

    telefono_contacto = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9+\-\s()]+$',
                message='El teléfono solo puede contener dígitos, +, -, paréntesis y espacios.',
            ),
        ],
        help_text='Teléfono de contacto'
    )

    tipo_solicitud = models.CharField(
        max_length=20,
        choices=TIPO_SOLICITUD_CHOICES,
        help_text='Categoría de la solicitud'
    )

    asunto = models.CharField(
        max_length=200,
        help_text='Resumen breve del tema de la solicitud'
    )

    descripcion_detallada = models.TextField(
        help_text='Descripción completa y detallada de la solicitud'
    )

    fecha_solicitud = models.DateField(
        auto_now_add=True,
        help_text='Fecha en que se registró la solicitud'
    )

    archivo_adjunto = models.FileField(
        upload_to='solicitudes_adjuntos/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'jpeg', 'png', 'txt'],
                message='Solo se permiten archivos PDF, DOC, DOCX, XLS, XLSX, JPG, JPEG, PNG o TXT.'
            )
        ],
        help_text='Archivo adjunto (opcional)'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha y hora de creación del registro'
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        help_text='Fecha y hora de última actualización'
    )

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto} ({self.get_tipo_solicitud_display()})"
