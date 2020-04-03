from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Aldeia, Suco, District
from .models import Aldeia, Suco, Subdistrict, District, Point, PhotoTimor, Istoriaviazen
from PIL import Image
from map.get_image_location import get_exif_data, get_lat_lon



class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(TemplateView, self).get_context_data(*args, *kwargs)

        # context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')

        context['viazen'] = Istoriaviazen.objects.all()
        # context['aldeias'] = serialize('geojson', Aldeia.objects.all(), geometry_field='geom')
        context['points'] = serialize('geojson', Point.objects.all(), geometry_field='geom')
        for photo in PhotoTimor.objects.all():
            get_data = get_exif_data(Image.open(photo.image.path))
            lat, lon = get_lat_lon(get_data)
            if lat and lon:
                images.append({"lat": lat, "lon": lon, "photo": photo.image.url})
        context['geoimages'] = images
        return context


class AnotherView(TemplateView):
    template_name = 'map/another.html'


class HatamaViazenView(CreateView):
    template_name = 'map/hatamaviazenview.html'
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'creator', 'people']
    success_url = "/"


    def get_context_data(self, *args, **kwargs):
        context = super(CreateView, self).get_context_data(*args, *kwargs)
        context['viazen'] = Istoriaviazen.objects.all()
        return context
