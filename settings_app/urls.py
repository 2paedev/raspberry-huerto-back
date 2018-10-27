from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from settings_app import views

urlpatterns = [
    path('manual/current', views.SettingsAppManualValues.as_view()),
    # path('auto-hours/current', views.SettingsAppAutoHoursValues.as_view()),
    # path('auto-humidity/current', views.SettingsAppAutoHumidityValues.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
