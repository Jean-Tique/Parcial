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

    def save(self, commit=True):
        user = super().save(commit=False)
        base_username = f"{user.first_name.lower()}.{user.last_name.lower()}"
        counter = 1
        username = base_username
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        user.username = username
        if commit:
            user.save()
        return user

        

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
