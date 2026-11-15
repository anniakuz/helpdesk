from django.db import models


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Incidencia(models.Model):
    ESTADOS = [
        ("abierto", "Abierto"),
        ("en_proceso", "En Proceso"),
        ("cerrado", "Cerrado"),
    ]
    PRIORIDADES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
        ("critica", "Critica"),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="abierto")
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default="media")
    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incidencias",
    )

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"#{self.pk} {self.titulo}"
