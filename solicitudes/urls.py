from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('crear/', views.solicitud_crear, name='solicitud_crear'),
    path('confirmacion/<int:solicitud_id>/', views.solicitud_confirmacion, name='solicitud_confirmacion'),
]
