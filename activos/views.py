from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Activo, Asignacion
from .forms import ActivoForm, AsignacionForm, UsuarioForm


def inicio(request):
    return render(request, "activos/inicio.html")


class ActivoListView(ListView):
    model = Activo
    template_name = "activos/lista.html"
    context_object_name = "activos"


class ActivoDetailView(DetailView):
    model = Activo
    template_name = "activos/detalle.html"


class ActivoCreateView(CreateView):
    model = Activo
    form_class = ActivoForm
    template_name = "activos/registrar_activo.html"
    success_url = reverse_lazy("activos:lista")

class ActivoUpdateView(UpdateView):
    model = Activo
    form_class = ActivoForm
    template_name = "activos/editar_activo.html"
    success_url = reverse_lazy("activos:lista")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asignacion = Asignacion.objects.filter(activo=self.object).last()
        context["asignacion_form"] = AsignacionForm(instance=asignacion)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        asignacion = Asignacion.objects.filter(activo=self.object).last()
        asignacion_form = AsignacionForm(request.POST, instance=asignacion)

        if form.is_valid() and asignacion_form.is_valid():
            form.save()
            asignacion = asignacion_form.save(commit=False)
            asignacion.activo = self.object   # 👈 fijamos activo manualmente
            asignacion.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class ActivoDeleteView(DeleteView):
    model = Activo
    template_name = "activos/eliminar_activo.html"
    success_url = reverse_lazy("activos:lista")


class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "activos/crear_usuario.html"
    success_url = reverse_lazy("activos:lista")


class UsuarioListView(ListView):
    model = User
    template_name = "activos/usuarios.html"
    context_object_name = "usuarios"


class AsignacionCreateView(CreateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = "activos/asignar_activo.html"
    success_url = reverse_lazy("activos:lista")

    def form_valid(self, form):
        asignacion = form.save(commit=False)
        asignacion.activo.estado = "Asignado"
        asignacion.activo.save()
        asignacion.save()
        return super().form_valid(form)
class UsuarioDeleteView(DeleteView):
    model = User
    template_name = "activos/eliminar_usuario.html"
    success_url = reverse_lazy("activos:lista_usuarios")
