from django.urls import path
from .views import (
    UsuarioDeleteView,
    inicio,
    ActivoListView,
    ActivoDetailView,
    ActivoCreateView,
    ActivoUpdateView,
    ActivoDeleteView,
    UsuarioCreateView, 
    UsuarioListView,
    AsignacionCreateView,
)

app_name = "activos"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("lista/", ActivoListView.as_view(), name="lista"),
    path("<int:pk>/", ActivoDetailView.as_view(), name="detalle"),
    path("registrar/", ActivoCreateView.as_view(), name="registrar"),
    path("usuario/", UsuarioCreateView.as_view(), name="usuario"),
    path("usuarios/", UsuarioListView.as_view(), name="lista_usuarios"),
    path("asignar/", AsignacionCreateView.as_view(), name="asignar"),
    path("activos/<int:pk>/editar/", ActivoUpdateView.as_view(), name="editar"),
    path("activos/<int:pk>/eliminar/", ActivoDeleteView.as_view(), name="eliminar"),
    path("usuarios/<int:pk>/eliminar/", UsuarioDeleteView.as_view(), name="eliminar_usuario"),

]
