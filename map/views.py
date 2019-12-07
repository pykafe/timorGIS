from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from .models import Suco, District

class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, *kwargs)

        context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')

        return context
