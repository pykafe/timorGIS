from django.conf import settings
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from map.models import District, PhotoTimor, IstoriaViazen

class VueView(TemplateView):
    template_name = 'vue_ui/index.html'

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context

def json_api(request):
    return JsonResponse({'hello': "world"})