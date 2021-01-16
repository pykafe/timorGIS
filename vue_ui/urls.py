from django.urls import path

from .views import VueView

urlpatterns = [
    path('', VueView.as_view(), name="home"),
]