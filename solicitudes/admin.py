from django.contrib import admin
from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Solicitud.
    Permite gestionar todas las solicitudes recibidas.
    """

    list_display = (
        'id',
        'nombre_solicitante',
        'tipo_solicitud',
        'asunto',
        'correo_electronico',
        'fecha_solicitud',
        'tiene_archivo',
    )

    list_filter = (
        'tipo_solicitud',
        'fecha_solicitud',
        'fecha_creacion',
    )

    search_fields = (
        'nombre_solicitante',
        'documento_identidad',
        'correo_electronico',
        'asunto',
    )

    readonly_fields = (
        'fecha_creacion',
        'fecha_actualizacion',
    )

    fieldsets = (
        ('Información del Solicitante', {
            'fields': (
                'nombre_solicitante',
                'documento_identidad',
                'correo_electronico',
                'telefono_contacto',
            )
        }),
        ('Detalles de la Solicitud', {
            'fields': (
                'tipo_solicitud',
                'asunto',
                'descripcion_detallada',
                'archivo_adjunto',
            )
        }),
        ('Fechas', {
            'fields': (
                'fecha_solicitud',
                'fecha_creacion',
                'fecha_actualizacion',
            ),
            'classes': ('collapse',)
        }),
    )

    def tiene_archivo(self, obj):
        """Muestra un indicador si la solicitud tiene archivo adjunto"""
        if obj.archivo_adjunto:
            return '✓ Sí'
        return '✗ No'

    tiene_archivo.short_description = 'Archivo Adjunto'
