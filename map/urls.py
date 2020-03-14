from django.urls import path
from .views import MapView, AnotherView, AddviazenView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
    path('viazen/', AddviazenView.as_view(), name='viazen'),
]
