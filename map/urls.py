from django.conf import settings
from django.urls import path
from .views import MapView, HatamaViazenView, PhotoViazenView, ViazenUpdateView, ViazenDeleteView, UpdatePhotoViazenView, DeletePhotoView, DetailMapView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('viazen/new', login_required(HatamaViazenView.as_view()), name='hatama_viazen'),
    path('viazen/update/<int:pk>', login_required(ViazenUpdateView.as_view()), name='update_viazen'),
    path('viazen/delete/<int:pk>', login_required(ViazenDeleteView.as_view()), name="delete_viazen"),
    path('photo/update/<int:pk>', login_required(UpdatePhotoViazenView.as_view()), name='update_photo'),
    path('photo/delete/<int:pk>', login_required(DeletePhotoView.as_view()), name='delete_photo'),
    path('viazen/<int:pk>/photo/new/', login_required(PhotoViazenView.as_view()), name='photo_viazen'),
    path('detail/viazen/<int:viazen_pk>/<int:photo_pk>', DetailMapView.as_view(), name="details"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
