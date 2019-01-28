from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Solicitudinteres)
admin.site.register(Detalleinteres)
admin.site.register(Encargado)

class AnimalAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

admin.site.register(Animal, AnimalAdmin)



# Register your models here.
