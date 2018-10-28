from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from settings_app import views

urlpatterns = [
    path('current', views.SettingsAppCurrentValues.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
