from .models import TemperatureAir
from rest_framework.views import APIView
from rest_framework.response import Response


class TemperatureAirList(APIView):
    def get(self, request, format=None):
        start_date = request.GET.get('startDate')
        end_date = request.GET.get('endDate')

        queryset = TemperatureAir.objects.all()
        all_data = [obj.as_dict() for obj in queryset]

        if start_date and end_date:
            queryset = TemperatureAir.objects.filter(
                created__range=[start_date, end_date])
            all_data = [obj.as_dict() for obj in queryset]

        return Response(all_data)
