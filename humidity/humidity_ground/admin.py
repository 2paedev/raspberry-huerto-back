from django.contrib import admin
from .models import HumidityGround


class HumidityGroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'value')
    readonly_fields = ('id', 'created',)


admin.site.register(HumidityGround, HumidityGroundAdmin)
