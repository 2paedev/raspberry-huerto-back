from rest_framework import serializers
from settings_app.models import SettingsApp


class SettingsAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsApp
        fields = ('id', 'setting_id', 'setting_value')
