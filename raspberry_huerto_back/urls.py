from django.urls import path, include

urlpatterns = [
    path('api/', include('card_info.urls')),
]
