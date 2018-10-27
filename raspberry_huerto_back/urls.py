from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/weather/', include('card_info.urls')),
    path('api/settings/', include('settings_app.urls')),
    path('admin/', admin.site.urls),
]
