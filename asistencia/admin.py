from django.contrib import admin
from .models import *


class DocenteAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    list_display = ('nombre', 'apellido', 'ci', 'num_ci')

class HorarioAdmin(admin.ModelAdmin):
    ordering = ('uc',)
    list_display = ('uc', 'docente', 'entrada', 'salida')
    
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Uc)