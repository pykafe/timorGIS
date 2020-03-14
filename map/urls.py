from django.urls import path
from .views import MapView, AnotherView, PostView

urlpatterns = [
    path('', MapView.as_view()),
    path('another', AnotherView.as_view()),
    path('journey_form', PostView.as_view(), name='journey_form'),
]
