from django.urls import path

from .views import VueView, AddIstoriaView, AddCommentView, geojson_api, images_api, istoriaviazen_api, login_api, commentphoto_api

urlpatterns = [
    path('', VueView.as_view(), name="home"),
    path('api/login', login_api, name="api_login"),
    path('api/geojson', geojson_api, name="api_geojson"),
    path('api/images', images_api, name="api_images"),
    path('api/istoriaviazen', istoriaviazen_api, name="api_istoriaviazen"),
    path('api/commentphoto', commentphoto_api, name="api_commentphoto"),
    path('api/add_istoria', AddIstoriaView.as_view(), name="api_add_istoria"),
    path('api/add_comment', AddCommentView.as_view(), name="api_add_comment"),
]
