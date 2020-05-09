from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from map.gps_images import ImageMetaData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aldeia, Suco, Subdistrict, District, PhotoTimor, Istoriaviazen
from django.urls import reverse_lazy
from django.http import Http404

class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, **kwargs)

        creator_filter = self.request.GET.get('creator', False)
        if creator_filter:
            try:
                context['creator_filter'] = User.objects.get(id=creator_filter)
                context['viazen'] = Istoriaviazen.objects.filter(creator=context['creator_filter'])
            except ValueError :
                raise Http404()
        else:
            context['viazen'] = Istoriaviazen.objects.all()


        context['users'] = User.objects.all()
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        images = []
        for photo in PhotoTimor.objects.filter(istoriaviazen__in=context['viazen']):
            get_data = ImageMetaData(photo.image.path)
            lat, lon = get_data.get_lat_lng()
            if lat and lon:
                images.append({"lat": lat, "lon": lon, "photo": photo.image.url, "viazen_id": photo.istoriaviazen_id})
        context['geoimages'] = images
        return context


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
