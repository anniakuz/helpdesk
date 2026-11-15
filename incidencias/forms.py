from django import forms

from .models import Incidencia


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ["titulo", "descripcion", "estado", "prioridad", "tecnico"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "prioridad": forms.Select(attrs={"class": "form-select"}),
            "tecnico": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()
        if len(titulo) < 5:
            raise forms.ValidationError("El titulo debe tener al menos 5 caracteres.")
        return titulo