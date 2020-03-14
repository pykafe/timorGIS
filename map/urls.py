from django.urls import path
from .views import MapView, AnotherView, HatamaViazenView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
    path('hatama_viazen/', HatamaViazenView.as_view(), name='hatama_viazen'),
]
