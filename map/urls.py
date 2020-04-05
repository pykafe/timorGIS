from django.conf import settings
from django.urls import path
from .views import MapView, AnotherView, HatamaViazenView, ViazenUpdateView, ViazenDeleteView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', MapView.as_view(), name="home"),
    path('another', AnotherView.as_view()),
    path('hatama_viazen/', HatamaViazenView.as_view(), name='hatama_viazen'),
    path('<int:pk>/update', ViazenUpdateView.as_view(), name='update_viazen'),
    path('<int:pk>/delete', ViazenDeleteView.as_view(), name="delete_viazen"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

