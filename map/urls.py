from django.urls import path
from .views import MapView, AnotherView, HatamaViazenView, delete_viazenview

urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('another', AnotherView.as_view()),
    path('hatama_viazen/', HatamaViazenView.as_view(), name='hatama_viazen'),
    path('<viazen_id>/delete', delete_viazenview, name="delete_viazen"),
]
