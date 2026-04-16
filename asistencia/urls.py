from django.urls import path

from . import views

app_name = 'asistencia'

urlpatterns = [
    path('registro/', views.asistencia_registro, name='registro'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
