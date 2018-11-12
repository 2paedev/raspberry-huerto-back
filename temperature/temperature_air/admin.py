from django.contrib import admin
from .models import TemperatureAir


class TemperatureAirAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'value')
    readonly_fields = ('id', 'created',)


admin.site.register(TemperatureAir, TemperatureAirAdmin)
