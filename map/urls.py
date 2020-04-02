from django.urls import path
from .views import MapView, AnotherView, HatamaViazenView, ViazenDeleteView

urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('another', AnotherView.as_view()),
    path('hatama_viazen/', HatamaViazenView.as_view(), name='hatama_viazen'),
    path('<int:pk>/delete', ViazenDeleteView.as_view(), name="delete_viazen"),
]
