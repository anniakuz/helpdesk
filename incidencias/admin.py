from django.contrib import admin
from .models import Incidencia, Tecnico


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especialidad", "email")
    search_fields = ("nombre", "especialidad", "email")


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "estado", "prioridad", "tecnico", "fecha_creacion")
    list_filter = ("estado", "prioridad")
    search_fields = ("titulo", "tecnico__nombre")
    date_hierarchy = "fecha_creacion"
