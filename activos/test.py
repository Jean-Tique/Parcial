from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from .models import Activo, Asignacion


class ActivoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username="jean", first_name="Jean", last_name="Tique")
        self.activo = Activo.objects.create(
            codigo="RC1234",
            descripcion="Portátil Lenovo",
            estado="Disponible"
        )

    def test_crear_activo(self):
        """Verifica que el activo se crea correctamente"""
        self.assertEqual(self.activo.codigo, "RC1234")
        self.assertEqual(self.activo.estado, "Disponible")

    def test_asignar_activo(self):
        """Verifica que se puede asignar un activo a un usuario"""
        asignacion = Asignacion.objects.create(
            activo=self.activo,
            usuario=self.usuario,
            fecha_entrega=date.today()
        )
        self.assertEqual(asignacion.usuario.username, "jean")
        self.assertEqual(asignacion.activo.codigo, "RC1234")

class ActivoViewsTest(TestCase):
    def setUp(self):
        self.activo = Activo.objects.create(
            codigo="RC5678",
            descripcion="Impresora HP",
            estado="Disponible"
        )

    def test_lista_activos_view(self):
        """Verifica que la vista de lista carga correctamente"""
        response = self.client.get(reverse("activos:lista"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista de Activos")

    def test_registrar_activo_view(self):
        """Verifica que se puede registrar un activo vía POST"""
        response = self.client.post(reverse("activos:registrar"), {
            "codigo": "RC9999",
            "descripcion": "Monitor Samsung",
            "estado": "Disponible"
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras guardar
        self.assertTrue(Activo.objects.filter(codigo="RC9999").exists())


class RegistrarActivoFormTest(TestCase):
    def test_registrar_activo_valido(self):
        """Verifica que se puede registrar un activo con datos válidos"""
        response = self.client.post(reverse("activos:registrar"), {
            "codigo": "RC1111",
            "descripcion": "Teclado Logitech",
            "estado": "Disponible"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Activo.objects.filter(codigo="RC1111").exists())

    def test_registrar_activo_invalido(self):
        """Verifica que no se puede registrar un activo sin código"""
        response = self.client.post(reverse("activos:registrar"), {
            "codigo": "",
            "descripcion": "Sin código",
            "estado": "Disponible"
        })
        self.assertEqual(response.status_code, 200)  # Se queda en la misma página
        self.assertContains(response, "Este campo es obligatorio")
