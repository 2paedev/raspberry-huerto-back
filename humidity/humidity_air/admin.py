from django.contrib import admin
from .models import HumidityAir


class HumidityAirAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'value')
    readonly_fields = ('created', 'id')


admin.site.register(HumidityAir, HumidityAirAdmin)
