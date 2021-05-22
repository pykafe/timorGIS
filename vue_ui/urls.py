from django.urls import path

from .views import VueView, geojson_api, images_api, istoriaviazen_api

urlpatterns = [
    path('', VueView.as_view(), name="home"),
    path('api/geojson', geojson_api, name="api_geojson"),
    path('api/images', images_api, name="api_images"),
    path('api/istoriaviazen', istoriaviazen_api, name="api_istoriaviazen"),
]