from .models import CardInfo
from .serializers import CardInfoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CardInfoList(APIView):
    def get(self, request, format=None):
        last_card_info = CardInfo.objects.latest()
        serializer = CardInfoSerializer(last_card_info)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from card_info.models import CardInfo
# from card_info.serializers import CardInfoSerializer
# from rest_framework import generics


# class CardInfoList(generics.ListCreateAPIView):
#     queryset = CardInfo.objects.all()
#     serializer_class = CardInfoSerializer


# class CardInfoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CardInfo.objects.all()
#     serializer_class = CardInfoSerializer
