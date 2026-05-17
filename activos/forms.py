from django import forms
from django.contrib.auth.models import User
from .models import Activo, Asignacion


class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ["codigo", "descripcion", "estado"]
        labels = {
            "codigo": "Código",
            "descripcion": "Descripción",
            "estado": "Estado",
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
        }

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ["usuario", "activo", "fecha_entrega"]
        labels = {
            "usuario": "Usuario",
            "activo": "Activo",
            "fecha_entrega": "Fecha de entrega",
        }
        widgets = {
            "fecha_entrega": forms.DateInput(attrs={"type": "date"})
        }
