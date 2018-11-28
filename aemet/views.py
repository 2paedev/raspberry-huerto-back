import json
import requests

from humidity.humidity_air.models import HumidityAir
from humidity.humidity_ground.models import HumidityGround
from temperature.temperature_air.models import TemperatureAir
from .config import AemetConfig

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

HEADERS = {'api_key': AemetConfig.AEMET_API_INFO['API_KEY']}
ERROR = {"status_code": 400, "message": "Aemet data not available"}


class AemetCityInfoList(APIView):
    url = AemetConfig.AEMET_API['MASTER']['SAN_VICENTE_RASPEIG']

    def get(self, request, format=None):
        r = requests.get(self.url, headers=HEADERS)
        if r.status_code == requests.codes.ok:
            return Response(r.json())
        return Response(data=json.dumps(ERROR), status=status.HTTP_200_OK)


class AemetPredictionList(APIView):
    url = AemetConfig.AEMET_API['PREDICTION']['DAILY']

    def get(self, request, format=None):
        r = requests.get(self.url, headers=HEADERS)
        if r.status_code == requests.codes.ok:
            prediction = r.json()
            data_response = self.get_prediction_data(prediction['datos'])
            return Response(data_response)
        return Response(data=json.dumps(ERROR), status=status.HTTP_200_OK)

    def get_prediction_data(self, url):
        data = requests.get(url)
        print(data.json())
        return data.json()
