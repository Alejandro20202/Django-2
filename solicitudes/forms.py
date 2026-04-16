from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    """
    Formulario ModelForm para la creación y edición de solicitudes.
    Incluye validación a nivel de formulario y widgets personalizados.
    """

    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento_identidad',
            'correo_electronico',
            'telefono_contacto',
            'tipo_solicitud',
            'asunto',
            'descripcion_detallada',
            'archivo_adjunto',
        ]
        widgets = {
            'nombre_solicitante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre completo',
                    'required': 'required',
                }
            ),
            'documento_identidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 12345678',
                    'required': 'required',
                }
            ),
            'correo_electronico': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'correo@ejemplo.com',
                    'required': 'required',
                }
            ),
            'telefono_contacto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: +57 (300) 123-4567',
                    'required': 'required',
                }
            ),
            'tipo_solicitud': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'asunto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Resumen breve de su solicitud',
                    'required': 'required',
                    'maxlength': '200',
                }
            ),
            'descripcion_detallada': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Describa en detalle su solicitud...',
                    'required': 'required',
                }
            ),
            'archivo_adjunto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': '.pdf,.doc,.docx,.xls,.xlsx,.jpg,.jpeg,.png,.txt',
                }
            ),
        }
        labels = {
            'nombre_solicitante': 'Nombre Completo',
            'documento_identidad': 'Documento de Identidad',
            'correo_electronico': 'Correo Electrónico',
            'telefono_contacto': 'Teléfono de Contacto',
            'tipo_solicitud': 'Tipo de Solicitud',
            'asunto': 'Asunto',
            'descripcion_detallada': 'Descripción Detallada',
            'archivo_adjunto': 'Archivo Adjunto (Opcional)',
        }
        help_texts = {
            'documento_identidad': 'Solo caracteres alfanuméricos',
            'telefono_contacto': 'Ej: +57 (300) 123-4567',
            'archivo_adjunto': 'Formatos permitidos: PDF, DOC, DOCX, XLS, XLSX, JPG, JPEG, PNG, TXT',
        }

    def clean_nombre_solicitante(self):
        """Validación adicional para nombre_solicitante"""
        nombre = self.cleaned_data.get('nombre_solicitante')
        if nombre and len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_telefono_contacto(self):
        """Validación adicional para telefono_contacto"""
        telefono = self.cleaned_data.get('telefono_contacto')
        if telefono and len(telefono) < 7:
            raise forms.ValidationError('El teléfono debe tener al menos 7 dígitos.')
        return telefono

    def clean_asunto(self):
        """Validación adicional para asunto"""
        asunto = self.cleaned_data.get('asunto')
        if asunto and len(asunto) < 5:
            raise forms.ValidationError('El asunto debe tener al menos 5 caracteres.')
        return asunto

    def clean_descripcion_detallada(self):
        """Validación adicional para descripción_detallada"""
        descripcion = self.cleaned_data.get('descripcion_detallada')
        if descripcion and len(descripcion) < 10:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion
