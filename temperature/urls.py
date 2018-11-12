from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from temperature.temperature_air import views as AirView

urlpatterns = [
    path('air', AirView.TemperatureAirList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
