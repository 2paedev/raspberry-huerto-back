from humidity.humidity_air.models import HumidityAir
from humidity.humidity_ground.models import HumidityGround
from temperature.temperature_air.models import TemperatureAir

from django.db import models


class CardInfo():
    humidity_air = HumidityAir
    humidity_ground = HumidityGround
    temperature_air = TemperatureAir

    class Meta:
        abstract = True
