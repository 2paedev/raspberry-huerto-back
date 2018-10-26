from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from card_info import views

urlpatterns = [
    path('weather/site/all', views.CardInfoList.as_view()),
    path('weather/site/all/<int:pk>', views.CardInfoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
