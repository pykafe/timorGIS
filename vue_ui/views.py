from django.conf import settings
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.core.cache import cache

from map.models import District, PhotoTimor, IstoriaViazen

class VueView(TemplateView):
    template_name = 'vue_ui/index.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'urls': dict(
                openstreetmap=settings.OPENSTREETMAP_URL,
                geojson=reverse("api_geojson"),
                images=reverse("api_images"),
                istoriaviazen=reverse("api_istoriaviazen"),
                media_url=settings.MEDIA_URL,
            )
        }
        return context

def geojson_api(request):
    cacheapi = cache.get('api_geojson')
    if cacheapi == None:
        geojson = cache.get_or_set('api_geojson', serialize('geojson', District.objects.all(), geometry_field='geom'))
    else:
        geojson = cache.get('api_geojson')
    response = HttpResponse(geojson, content_type="application/json")
    return response

def images_api(request):
    cacheapi = cache.get('api_images')
    if cacheapi == None:
        json = cache.get_or_set('api_images', serialize('json', PhotoTimor.objects.all()))
    else:
        json = cache.get('api_images')
    response = HttpResponse(json, content_type="application/json")
    return response

def istoriaviazen_api(request):
    cacheapi = cache.get('api_istoriaviazen')
    if cacheapi == None:
        json = cache.get_or_set('api_istoriaviazen', serialize('json', IstoriaViazen.objects.all()))
    else:
        json = cache.get('api_istoriaviazen')
    response = HttpResponse(json, content_type="application/json")
    return response
