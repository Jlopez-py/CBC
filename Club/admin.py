from django.contrib import admin
from .models import Equip,Jugador

class EquipAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'equip', 'numero_licencia')
    search_fields = ('nom_complet',)
    list_filter = ('equip',)


admin.site.register(Equip, EquipAdmin)
admin.site.register(Jugador, JugadorAdmin)

