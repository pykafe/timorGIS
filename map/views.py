from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from map.gps_images import ImageMetaData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aldeia, Suco, Subdistrict, District, PhotoTimor, Istoriaviazen
from django.contrib.gis.geos import Point
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


def queryobject(obj, lon, lat):
    queryset = obj.objects.filter(geom__contains=Point(lon, lat))
    return ",".join([str(instance) for instance in queryset])

def serializes(obj, name):
    return serialize('geojson', obj.objects.filter(name=name), geometry_field='geom')


class DetailMapView(TemplateView):
    template_name = 'map/details.html'

    def get_context_data(self, *args, **kwargs):

        context = super(DetailMapView, self).get_context_data(*args, **kwargs)
        images = []
        photo_id = kwargs['pk']
        try:
            context['photoviazen'] = PhotoTimor.objects.get(id=photo_id)
            target = context['photoviazen'].istoriaviazen_id
        except:
            target = photo_id
        context['viazen'] = Istoriaviazen.objects.get(id=target)
        for photo in PhotoTimor.objects.filter(istoriaviazen=target):
            get_data = ImageMetaData(photo.image.path)
            lat, lon = get_data.get_lat_lng()
            if lat and lon:
                suco = queryobject(Suco, lon, lat)
                subdistrict = queryobject(Subdistrict, lon, lat)
                district = queryobject(District, lon, lat)
                images.append({"lat": lat,
                                "lon": lon,
                               "photo": photo.image.url,
                               "photo_id": photo.pk,
                               "viazen_id": photo.istoriaviazen_id,
                               "suco": suco,
                               "subdistrict": subdistrict,
                               "district": district,
                })
                if photo_id == photo.pk:
                    context['districts'] = serializes(District, district)
                    context['subdistrict'] = serializes(Subdistrict, subdistrict)
                    context['suco'] = serializes(Suco, suco)
                    context['points'] = {
                        'DEFAULT_CENTER': [lat, lon,10],
                        'DEFAULT_ZOOM': 10,
                    }

        context['geoimages'] = images
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context


class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(MapView, self).get_context_data(*args, **kwargs)

        context['users'] = User.objects.all()
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        context['viazen'] = Istoriaviazen.objects.all()
        for photo in PhotoTimor.objects.all():
            get_data = ImageMetaData(photo.image.path)
            lat, lon = get_data.get_lat_lng()
            if lat and lon:
                suco = queryobject(Suco, lon, lat)
                subdistrict = queryobject(Subdistrict, lon, lat)
                district = queryobject(District, lon, lat)
                images.append({"lat": lat,
                               "lon": lon,
                               "photo": photo.image.url,
                               "photo_id": photo.pk,
                               "viazen_id": photo.istoriaviazen_id,
                               "suco": suco,
                               "subdistrict": subdistrict,
                               "district": district,
                })
        context['geoimages'] = images
        context['points'] = {
            'DEFAULT_CENTER': [-8.8315139, 125.6199236,8],
            'DEFAULT_ZOOM': 8,
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hatama_viazen'] = _("Add Journey History")
        return context


class PhotoViazenView(CreateView):
    template_name = 'map/phototimor_form.html'
    model = PhotoTimor
    fields = ['image', 'istoriaviazen']

    def get_success_url(self):
        return reverse_lazy('photo_viazen', args = (self.object.istoriaviazen_id,))

    def get_context_data(self, *args, **kwargs):
        target = self.kwargs['pk']
        context = super(PhotoViazenView, self).get_context_data(*args, **kwargs)
        context['journey_photos'] = PhotoTimor.objects.filter(istoriaviazen=target)
        return context


class ViazenUpdateView(UpdateView):
    template_name = 'map/viajen_form.html'
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'creator']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['update_viazen'] = _("Update Journey History")
        return context


class ViazenDeleteView(DeleteView):
    model = Istoriaviazen
    success_url = reverse_lazy('home')
