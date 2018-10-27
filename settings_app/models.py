from django.db import models
from django.db.models.fields import PositiveSmallIntegerField

SETTING_CHOICES = (
    (0, 'Manual'),
    (1, 'Auto Hours'),
    (2, 'Auto Humidity'),
)

SETTING_VALUES_CHOICES = (
    (0, 'OFF'),
    (1, 'ON'),
)


class SettingsApp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    setting_id = models.PositiveSmallIntegerField(
        choices=SETTING_CHOICES, default=0)
    value = models.PositiveSmallIntegerField(
        choices=SETTING_VALUES_CHOICES, default=0)

    class Meta:
        ordering = ('created',)
        get_latest_by = ('created',)
