from django.test import TestCase
from .models import Desarrollo  # Importa el modelo correcto

class DesarrolloModelTest(TestCase):

    def setUp(self):
        # Crear una instancia de Desarrollo para usar en las pruebas
        self.desarrollo = Desarrollo.objects.create(
            titulo='Proyecto Ejemplo',
            contenido='Descripción del proyecto de ejemplo.',
            imagen='ruta/a/imagen.jpg',
            brochurePaper='ruta/a/brochure.pdf',
        )

    def test_desarrollo_creation(self):
        # Verifica que el desarrollo fue creado correctamente
        self.assertEqual(self.desarrollo.titulo, 'Proyecto Ejemplo')
        self.assertEqual(self.desarrollo.contenido, 'Descripción del proyecto de ejemplo.')