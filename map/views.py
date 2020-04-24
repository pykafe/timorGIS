from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from map.gps_images import ImageMetaData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aldeia, Suco, Subdistrict, District, Point, PhotoTimor, Istoriaviazen
from django.contrib.gis.geos import Point as P
from django.urls import reverse_lazy
from django.shortcuts import render_to_response
from django.conf import settings

def queryobject(obj, lon, lat):
    queryset = obj.objects.filter(geom__contains=P(lon, lat))
    return "".join([str(query) for query in queryset])


class DetailMapView(TemplateView):
    template_name = 'map/details.html'

    def get_context_data(self, *args, **kwargs):

        context = super(DetailMapView, self).get_context_data(*args, **kwargs)
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        context['points'] = {
            'DEFAULT_CENTER': [-8.8315139, 125.6199236,10],
            'DEFAULT_ZOOM': 10,
        }
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context


class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(MapView, self).get_context_data(*args, **kwargs)

        context['users'] = User.objects.all()
        # context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')

        context['viazen'] = Istoriaviazen.objects.all()
        # context['aldeias'] = serialize('geojson', Aldeia.objects.all(), geometry_field='geom')
        context['points'] = serialize('geojson', Point.objects.all(), geometry_field='geom')
        for photo in PhotoTimor.objects.all():
            get_data = ImageMetaData(photo.image.path)
            lat, lon = get_data.get_lat_lng()
            aldeia =queryobject(Aldeia, lon, lat)
            suco = queryobject(Suco, lon, lat)
            subdistrict = queryobject(Subdistrict, lon, lat)
            district = queryobject(District, lon, lat)
            if lat and lon:
                images.append({"lat": lat,
                               "lon": lon,
                               "photo": photo.image.url,
                               "viazen_id": photo.istoriaviazen_id,
                               "aldeia": aldeia,
                               "suco": suco,
                               "subdistrict": subdistrict,
                               "district": district,
                })
        context['geoimages'] = images
        context['points'] = {
            'DEFAULT_CENTER': [-8.8315139, 125.6199236,9],
            'DEFAULT_ZOOM': 9,
        }
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context


class AnotherView(TemplateView):
    template_name = 'map/another.html'


class HatamaViazenView(CreateView):
    template_name = 'map/viajen_form.html'
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'creator']

    def get_success_url(self):
        return reverse_lazy('photo_viazen', args = (self.object.id,))


class PhotoViazenView(CreateView):
    template_name = 'map/phototimor_form.html'
    model = PhotoTimor
    fields = ['istoriaviazen', 'image']

    def get_success_url(self):
        return reverse_lazy('photo_viazen', args = (self.object.istoriaviazen_id,))


class ViazenUpdateView(UpdateView):
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'creator']
    success_url = reverse_lazy('home')


class ViazenDeleteView(DeleteView):
    model = Istoriaviazen
    success_url = reverse_lazy('home')
