from django.urls import path
from .views import MapView, AnotherView, KriaviajenView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
    path('kria_viajen/', KriaviajenView.as_view(), name='kria_viajen'),
]
