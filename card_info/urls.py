from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from card_info import views

urlpatterns = [
    path('site/all', views.CardInfoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
