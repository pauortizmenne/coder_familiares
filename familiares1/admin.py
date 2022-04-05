from django.contrib import admin
from .models import Familia

# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'fecha')

admin.site.register(Familia, FamiliaAdmin)