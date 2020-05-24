from django.conf import settings
from django.urls import path
from .views import MapView, HatamaViazenView, PhotoViazenView, ViazenUpdateView, ViazenDeleteView, DetailMapView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('hatama_viazen/', login_required(HatamaViazenView.as_view()), name='hatama_viazen'),
    path('<int:pk>/update', login_required(ViazenUpdateView.as_view()), name='update_viazen'),
    path('<int:pk>/photo_viazen/', login_required(PhotoViazenView.as_view()), name='photo_viazen'),
    path('<int:pk>/delete', login_required(ViazenDeleteView.as_view()), name="delete_viazen"),
    path('detail/viazen/<int:viazen_pk>/<int:photo_pk>', DetailMapView.as_view(), name="details"),

]
