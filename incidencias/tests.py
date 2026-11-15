from django.test import TestCase
from django.urls import reverse
from .models import Incidencia, Tecnico


class IncidenciaTests(TestCase):
    def setUp(self):
        self.tecnico = Tecnico.objects.create(
            nombre="Marta Ruiz", especialidad="Redes", email="marta@example.com"
        )

    def test_lista_muestra_incidencias(self):
        Incidencia.objects.create(
            titulo="Sin conexion", descripcion="No hay red", tecnico=self.tecnico
        )
        r = self.client.get(reverse("incidencias:lista"))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Sin conexion")

    def test_formulario_campos_vacios(self):
        r = self.client.post(reverse("incidencias:nueva"), {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Incidencia.objects.count(), 0)
        self.assertContains(r, "Este campo es obligatorio")

    def test_formulario_crea_incidencia(self):
        r = self.client.post(
            reverse("incidencias:nueva"),
            {
                "titulo": "Impresora atascada",
                "descripcion": "Papel atascado",
                "estado": "abierto",
                "prioridad": "alta",
                "tecnico": self.tecnico.pk,
            },
        )
        self.assertRedirects(r, reverse("incidencias:lista"))
        self.assertEqual(Incidencia.objects.count(), 1)
