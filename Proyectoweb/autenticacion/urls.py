from django.urls import path
from .views import VRegistro, cerrar_sesion, logear

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),  # Vista basada en clase, correcto usar as_view()
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),  # Vista basada en función, eliminar as_view()
    path('logear', logear, name="logear"),  # Vista basada en función, eliminar as_view()
]