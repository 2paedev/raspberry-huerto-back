from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from aemet import views

urlpatterns = [
    path('city-info', views.AemetCityInfoList.as_view()),
    path('prediction', views.AemetPredictionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
