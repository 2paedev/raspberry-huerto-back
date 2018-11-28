from django.db import models


class CityInfo(models.Model):
    name = models.CharField()
    latitude = models.CharField()
    latitude_dec = models.CharField()
    longitude = models.CharField()
    longitude_dec = models.CharField()
    altitude = models.CharField()
    residents_number = models.CharField()

    class Meta:
        ordering = ('name',)


class Prediction(models.Model):
    update = models.DateTimeField(auto_now_add=True)
    data = models.URLField()

    class Meta:
        ordering = ('update',)
        get_latest_by = ('update',)
