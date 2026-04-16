from django.shortcuts import redirect, render

from .forms import AsistenciaForm


def asistencia_registro(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia:confirmacion')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia/asistencia_form.html', {'form': form})


def confirmacion(request):
    return render(request, 'asistencia/confirmacion.html')
