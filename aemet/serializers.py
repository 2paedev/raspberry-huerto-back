from rest_framework import serializers
from .models import CityInfo, Prediction


class AemetCityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityInfo
        fields = ('id',)


class AemetPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('id',)
