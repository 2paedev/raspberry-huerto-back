from rest_framework import serializers
from card_info.models import CardInfo


class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = ('id', 'humidity_air', 'humidity_ground', 'temperature_air')
