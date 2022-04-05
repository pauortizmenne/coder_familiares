from django.urls import include, path
from .views import listado_familiares

urlpatterns = [
    path('familiares/', listado_familiares)
]