from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from humidity.humidity_air import views as AirView
from humidity.humidity_ground import views as GroundView

urlpatterns = [
    path('air', AirView.HumidityAirList.as_view()),
    path('ground', GroundView.HumidityGroundList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
