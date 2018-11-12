from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat


class WeatherMeasures(models.Model):
    created = models.DateTimeField(
        auto_now_add=True)

    value = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        default=0)

    def as_dict(self):
        date_formatted = DateFormat(self.created)
        return {
            'id': self.id,
            'created': date_formatted.format('Y-m-d'),
            'value': str(self.value)
        }

    class Meta:
        abstract = True
        ordering = ('created',)
        get_latest_by = ('created',)
