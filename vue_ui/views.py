from django.db.models import Max
from django.conf import settings
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import last_modified
from django.views.generic.base import TemplateView
from django.urls import reverse

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
    geojson = serialize('geojson', District.objects.all(), geometry_field='geom')
    response = HttpResponse(geojson, content_type="application/json")
    return response

def images_modified_at(request):
    ''' returns the last time the photo objects were modified '''
    return PhotoTimor.objects.aggregate(Max('modified_at'))['modified_at__max']

@last_modified(images_modified_at)
def images_api(request):
    json = serialize('json', PhotoTimor.objects.all())
    response = HttpResponse(json, content_type="application/json")
    return response

def istoriaviazen_api(request):
    json = serialize('json', IstoriaViazen.objects.all())
    response = HttpResponse(json, content_type="application/json")
    return response