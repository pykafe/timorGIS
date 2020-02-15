from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from .models import Aldeia, Suco, District
from .models import Aldeia, Suco, Subdistrict, District, Point, PhotoTimor
from PIL import Image
from map.get_image_location import get_exif_data, get_lat_lon



class MapView(TemplateView):
    template_name = 'map/base.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(TemplateView, self).get_context_data(*args, *kwargs)

        # context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        # context['aldeias'] = serialize('geojson', Aldeia.objects.all(), geometry_field='geom')
        context['points'] = serialize('geojson', Point.objects.all(), geometry_field='geom')
        for  photo in PhotoTimor.objects.all():
            photos = "media/"+str(photo)
            get_data = get_exif_data(Image.open(photos))
            (lat, lon) = get_lat_lon(get_data)
            images.append({"lat": lat, "lon": lon, "photo": photos})
        context['geoimages'] = images
        return context
