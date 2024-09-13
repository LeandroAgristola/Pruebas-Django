from django.urls import path
from . import views

urlpatterns = [
    path('', views.VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('logear/', views.logear, name='logear'),
]