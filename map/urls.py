from django.conf import settings
from django.urls import path
from .views import MapView, HatamaViazenView, PhotoViazenView, ViazenUpdateView, ViazenDeleteView, UpdatePhotoViazenView, DeletePhotoView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('viazen/new', HatamaViazenView.as_view(), name='hatama_viazen'),
    path('viazen/update/<int:pk>', ViazenUpdateView.as_view(), name='update_viazen'),
    path('viazen/delete/<int:pk>', ViazenDeleteView.as_view(), name="delete_viazen"),
    path('photo/update/<int:pk>', UpdatePhotoViazenView.as_view(), name='update_photo'),
    path('photo/delete/<int:pk>', DeletePhotoView.as_view(), name='delete_photo'),
    path('viazen/<int:pk>/photo/new/', PhotoViazenView.as_view(), name='photo_viazen'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
