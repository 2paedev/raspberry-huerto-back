from .models import SettingsApp
from .serializers import SettingsAppSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


class SettingsAppCurrentValues(APIView):
    def get(self, request, format=None):
        last_setting = SettingsApp.objects.latest()
        serializer = SettingsAppSerializer(last_setting)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SettingsAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
