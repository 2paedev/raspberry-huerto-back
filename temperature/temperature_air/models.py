from common.models.weather_measures import WeatherMeasures
from django.db import models


class TemperatureAir(WeatherMeasures, models.Model):
    pass
