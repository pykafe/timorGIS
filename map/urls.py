from django.conf import settings
from django.urls import path
from .views import MapView, HatamaViazenView, PhotoViazenView, ViazenUpdateView, ViazenDeleteView, DeletePhotoView, DetailMapView, FullMapView, StyleGuideView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('viazen/new', login_required(HatamaViazenView.as_view()), name='hatama_viazen'),
    path('viazen/update/<int:pk>', login_required(ViazenUpdateView.as_view()), name='update_viazen'),
    path('viazen/delete/<int:pk>', login_required(ViazenDeleteView.as_view()), name="delete_viazen"),
    path('photo/delete/<int:pk>', login_required(DeletePhotoView.as_view()), name='delete_photo'),
    path('viazen/<int:pk>/photo/new/', login_required(PhotoViazenView.as_view()), name='photo_viazen'),
    path('detail/viazen/<int:viazen_pk>/<int:photo_pk>', DetailMapView.as_view(), name="details"),
    path('fullmap/', FullMapView.as_view(), name="fullmap"),
    path('style_guide', StyleGuideView.as_view(), name='style_guide'),
]
