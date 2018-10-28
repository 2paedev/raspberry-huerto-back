from .models import CardInfo
from .serializers import CardInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CardInfoList(APIView):
    def get(self, request, format=None):
        last_card_info = CardInfo.objects.latest()
        serializer = CardInfoSerializer(last_card_info)
        return Response(serializer.data)
