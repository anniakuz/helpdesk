from django.urls import path

from . import views

app_name = "incidencias"

urlpatterns = [
    path("", views.IncidenciaListView.as_view(), name="lista"),
    path("nueva/", views.IncidenciaCreateView.as_view(), name="nueva"),
]