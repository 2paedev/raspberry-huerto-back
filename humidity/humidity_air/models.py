from common.models.weather_measures import WeatherMeasures
from django.db import models


class HumidityAir(WeatherMeasures, models.Model):
    pass
