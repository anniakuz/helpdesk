from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import IncidenciaForm
from .models import Incidencia


class IncidenciaListView(ListView):
    model = Incidencia
    template_name = "incidencias/lista.html"
    context_object_name = "incidencias"


class IncidenciaCreateView(CreateView):
    model = Incidencia
    form_class = IncidenciaForm
    template_name = "incidencias/formulario.html"
    success_url = reverse_lazy("incidencias:lista")

    def form_valid(self, form):
        messages.success(self.request, "Incidencia registrada correctamente.")
        return super().form_valid(form)