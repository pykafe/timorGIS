from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from .models import Aldeia, Suco, District
from .models import Aldeia, Suco, Subdistrict, District, Point, PhotoTimor
from PIL import Image
from map.get_image_location import get_exif_data, get_lat_lon
from map.forms import IstoriaviazenForm
from django.http import HttpResponse


class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(TemplateView, self).get_context_data(*args, *kwargs)

        # context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        # context['aldeias'] = serialize('geojson', Aldeia.objects.all(), geometry_field='geom')
        context['points'] = serialize('geojson', Point.objects.all(), geometry_field='geom')
        for photo in PhotoTimor.objects.all():
            get_data = get_exif_data(Image.open(photo.image.path))
            lat, lon = get_lat_lon(get_data)
            if lat and lon:
                images.append({"lat": lat, "lon": lon, "photo": photo.image.url})
        context['geoimages'] = images
        context['istoriaviazen'] = IstoriaviazenForm()
        return context


def viazenview(request):

    return HttpResponse("Hello world")

