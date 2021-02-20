from django.urls import path

from .views import VueView, json_api

urlpatterns = [
    path('', VueView.as_view(), name="home"),
    path('api', json_api, name="api"),
]