from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CardInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    humidity_air = models.DecimalField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        decimal_places=2,
        max_digits=3,
        default=0)
    humidity_ground = models.DecimalField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        decimal_places=2,
        max_digits=3,
        default=0)
    temperature_air = models.DecimalField(
        validators=[MinValueValidator(-100.0), MaxValueValidator(100.0)],
        decimal_places=2,
        max_digits=3,
        default=100)

    class Meta:
        ordering = ('created',)
