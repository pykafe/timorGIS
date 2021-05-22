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
    geojson = cache.get('api_geojson')
    if geojson == None:
        geojson = serialize('geojson', District.objects.all(), geometry_field='geom')
        cache.set('api_geojson', geojson)
    response = HttpResponse(geojson, content_type="application/json")
    return response

def images_api(request):
    images = [
        {
            "id": photo["id"],
            "image": photo["image"],
            "istoria": {
                "id": photo["istoriaviazen_id"],
                "title": photo["istoriaviazen__title"],
            }
        }
        for photo in PhotoTimor.objects.values(
            'id',
            'image',
            'istoriaviazen_id',
            'istoriaviazen__title',
        )
    ]
    response = JsonResponse(images, safe=False)
    return response

def istoriaviazen_api(request):
    json = serialize('json', IstoriaViazen.objects.all())
    response = HttpResponse(json, content_type="application/json")
    return response
