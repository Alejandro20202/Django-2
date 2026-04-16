from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Solicitud
from .forms import SolicitudForm


@require_http_methods(["GET", "POST"])
def solicitud_crear(request):
    """
    Vista para crear una nueva solicitud.
    GET: Muestra el formulario vacío
    POST: Procesa el formulario y guarda la solicitud en la BD
    """
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                solicitud = form.save(commit=False)
                solicitud.save()
                messages.success(request, 'Solicitud registrada exitosamente.')
                return redirect('solicitudes:solicitud_confirmacion', solicitud_id=solicitud.id)
            except Exception as e:
                messages.error(request, f'Error al guardar la solicitud: {str(e)}')
                return redirect('solicitudes:solicitud_crear')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = SolicitudForm()

    context = {
        'form': form,
        'titulo': 'Crear Nueva Solicitud',
    }
    return render(request, 'solicitudes/solicitud_form.html', context)


@require_http_methods(["GET"])
def solicitud_confirmacion(request, solicitud_id):
    """
    Vista para mostrar la confirmación de una solicitud registrada.
    Muestra los detalles de la solicitud guardada.
    """
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
    except Solicitud.DoesNotExist:
        messages.error(request, 'La solicitud no fue encontrada.')
        return redirect('solicitudes:solicitud_crear')

    context = {
        'solicitud': solicitud,
        'titulo': 'Confirmación de Solicitud',
    }
    return render(request, 'solicitudes/confirmacion.html', context)
