from humidity.humidity_air.models import HumidityAir
from humidity.humidity_ground.models import HumidityGround
from temperature.temperature_air.models import TemperatureAir
from .serializers import CardInfoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class CardInfoList(APIView):
    def get(self, request, format=None):
        try:
            last_humidity_air = str(HumidityAir.objects.latest().value)
        except HumidityAir.DoesNotExist:
            last_humidity_air = -1000

        try:
            last_humidity_ground = str(HumidityGround.objects.latest().value)
        except HumidityGround.DoesNotExist:
            last_humidity_ground = -1000

        try:
            last_temperature_air = str(TemperatureAir.objects.latest().value)
        except TemperatureAir.DoesNotExist:
            last_temperature_air = -1000

        all_last_data = {
            'humidity_air': last_humidity_air,
            'humidity_ground': last_humidity_ground,
            'temperature_air': last_temperature_air,
        }
        return Response(all_last_data)
