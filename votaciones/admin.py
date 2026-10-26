from django.contrib import admin
from .models import Edicion, Categoria, Votacion, Opcion

admin.site.register(Edicion)
admin.site.register(Categoria)
admin.site.register(Votacion)
admin.site.register(Opcion)
from .models import Voto
@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'votacion', 'opcion', 'fecha')
    list_filter = ('votacion',)
    readonly_fields = ('usuario', 'votacion', 'opcion', 'fecha')
    def has_add_permission(self, request):
        return False
