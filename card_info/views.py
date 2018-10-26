from card_info.models import CardInfo
from card_info.serializers import CardInfoSerializer
from rest_framework import generics


class CardInfoList(generics.ListCreateAPIView):
    queryset = CardInfo.objects.all()
    serializer_class = CardInfoSerializer


class CardInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardInfo.objects.all()
    serializer_class = CardInfoSerializer
