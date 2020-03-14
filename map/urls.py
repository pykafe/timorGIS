from django.urls import path
from .views import MapView, AnotherView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
]
