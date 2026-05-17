from django import forms
from django.contrib.auth.models import User
from .models import Activo, Asignacion

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ["codigo", "descripcion", "estado"]

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
        base = f"{user.first_name.lower()}.{user.last_name.lower()}"
        username = base
        n = 1
        while User.objects.filter(username=username).exists():
            username = f"{base}{n}"
            n += 1
        user.username = username
        if commit:
            user.save()
        return user

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ["usuario","activo", "fecha_entrega"]  # 👈 solo usuario y fecha
        labels = {
            "usuario": "Usuario",
            "fecha_entrega": "Fecha de entrega",
        }
        widgets = {
            "fecha_entrega": forms.DateInput(attrs={"type": "date"})
        }
