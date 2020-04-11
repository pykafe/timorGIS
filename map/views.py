from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from map.gps_images import ImageMetaData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aldeia, Suco, Subdistrict, District, Point, PhotoTimor, Istoriaviazen
from django.urls import reverse_lazy


class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(TemplateView, self).get_context_data(*args, **kwargs)

        # context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')

        context['viazen'] = Istoriaviazen.objects.all()
        # context['aldeias'] = serialize('geojson', Aldeia.objects.all(), geometry_field='geom')
        context['points'] = serialize('geojson', Point.objects.all(), geometry_field='geom')
        for photo in PhotoTimor.objects.all():
            get_data = ImageMetaData(photo.image.path)
            lat, lon = get_data.get_lat_lng()
            if lat and lon:
                images.append({"lat": lat, "lon": lon, "photo": photo.image.url})
        context['geoimages'] = images
        return context


class AnotherView(TemplateView):
    template_name = 'map/another.html'


class HatamaViazenView(CreateView):
    template_name = 'map/hatamaviazenview.html'
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'image_trip']
    success_url = reverse_lazy('home')


class ViazenUpdateView(UpdateView):
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'creator', 'image_trip']
    success_url = reverse_lazy('home')


class ViazenDeleteView(DeleteView):
    model = Istoriaviazen
    success_url = reverse_lazy('home')
