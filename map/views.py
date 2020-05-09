from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from map.gps_images import ImageMetaData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Aldeia, Suco, Subdistrict, District, PhotoTimor, Istoriaviazen
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(TemplateView, self).get_context_data(*args, **kwargs)

        context['users'] = User.objects.all()
        # context['sucos'] = serialize('geojson', Suco.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')

        context['viazen'] = Istoriaviazen.objects.all()
        # context['aldeias'] = serialize('geojson', Aldeia.objects.all(), geometry_field='geom')
        for photo in PhotoTimor.objects.all():
            get_data = ImageMetaData(photo.image.path)
            lat, lon = get_data.get_lat_lng()
            if lat and lon:
                images.append({"lat": lat, "lon": lon, "photo": photo.image.url, "viazen_id": photo.istoriaviazen_id, "photo_id": photo.pk })
        context['geoimages'] = images
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

class UpdatePhotoViazenView(UpdateView):
    template_name = 'map/updatephototimor_form.html'
    model = PhotoTimor
    fields = ['image', 'istoriaviazen']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        target = self.kwargs['pk']
        context = super(UpdatePhotoViazenView, self).get_context_data(*args, **kwargs)
        context['journey_photos'] = PhotoTimor.objects.filter(id=target)
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


class DeletePhotoView(DeleteView):
    model = PhotoTimor
    template_name = 'map/istoriaviazen_confirm_delete.html'
    success_url = reverse_lazy('home')
