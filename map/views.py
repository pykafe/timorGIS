from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from map.gps_images import ImageMetaData
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import District, PhotoTimor, IstoriaViazen
from django.urls import reverse_lazy
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class FullMapView(TemplateView):
    template_name = 'map/fullmapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(FullMapView, self).get_context_data(*args, **kwargs)
        context['viazen'] = IstoriaViazen.objects.all()
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        context['images'] = PhotoTimor.objects.filter(istoriaviazen__in=context['viazen'])
        context['points'] = {
            'DEFAULT_CENTER': [-8.8315139, 125.6199236,9],
            'DEFAULT_ZOOM': 9,
        }
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context



class DetailMapView(TemplateView):
    template_name = 'map/details.html'

    def get_context_data(self, *args, **kwargs):

        context = super(DetailMapView, self).get_context_data(*args, **kwargs)
        images = []
        photo_pk = kwargs['photo_pk']
        viazen_pk = kwargs['viazen_pk']
        try:
            viazen = IstoriaViazen.objects.get(pk=viazen_pk)
        except ObjectDoesNotExist:
            raise Http404()
        if photo_pk == 0:
            selected_photo = viazen.photos.first()
        else:
            try:
                selected_photo = viazen.photos.get(pk=photo_pk)
            except ObjectDoesNotExist:
                raise Http404()


        context['districts'] = serialize('geojson', selected_photo.districts(), geometry_field='geom')
        context['subdistricts'] = serialize('geojson', selected_photo.subdistricts(), geometry_field='geom')
        context['sucos'] = serialize('geojson', selected_photo.sucos(), geometry_field='geom')
        context['DEFAULT_CENTER'] = [selected_photo.point().y, selected_photo.point().x, 10]
        context['DEFAULT_ZOOM'] = 10

        context['viazen'] = viazen
        context['selected_photo'] = selected_photo
        context['geoimages'] = images
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context


class MapView(TemplateView):
    template_name = 'map/mapview.html'

    def get_context_data(self, *args, **kwargs):
        images = []
        context = super(MapView, self).get_context_data(*args, **kwargs)

        creator_filter = self.request.GET.get('creator', False)
        if creator_filter:
            try:
                context['creator_filter'] = User.objects.get(id=creator_filter)
                context['viazen'] = IstoriaViazen.objects.filter(creator=context['creator_filter']).order_by('-created_at')
            except (ValueError, ObjectDoesNotExist):
                raise Http404()
        else:
            context['viazen'] = IstoriaViazen.objects.all().order_by('-created_at')

        context['users'] = IstoriaViazen.objects.distinct('creator')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        context['images'] = PhotoTimor.objects.filter(istoriaviazen__in=context['viazen'])
        context['points'] = {
            'DEFAULT_CENTER': [-8.8315139, 125.6199236,8],
            'DEFAULT_ZOOM': 8,
        }
        context['url_openstreetmap'] = settings.OPENSTREETMAP_URL
        return context


class HatamaViazenView(CreateView):
    template_name = 'map/viajen_form.html'
    model = IstoriaViazen
    fields = ['title', 'description', 'duration_of_trip']

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hatama_viazen'] = _("Add Journey History")

        return context

    def form_valid(self, form):

        # set the creator of the istoria to the logged in user
        form.instance.creator = self.request.user

        redirect = super().form_valid(form)

        for photo_file in self.request.FILES.getlist('photos'):
            photo = PhotoTimor.objects.create(istoriaviazen=self.object, image=photo_file)
            self.object.photos.add(photo)

        return redirect


class PhotoViazenView(CreateView):
    template_name = 'map/phototimor_form.html'
    model = PhotoTimor
    fields = ['image']

    def get_success_url(self):
        return reverse_lazy('photo_viazen', args = (self.object.istoriaviazen_id,))

    def get_context_data(self, *args, **kwargs):
        target = self.kwargs['pk']
        context = super(PhotoViazenView, self).get_context_data(*args, **kwargs)
        context['journey_photos'] = PhotoTimor.objects.filter(istoriaviazen=target)
        return context

    def form_valid(self, form):
        # set the viazen of the photo to the url viazen
        form.instance.istoriaviazen_id = self.kwargs['pk']
        return super().form_valid(form)


class UpdatePhotoViazenView(UpdateView):
    template_name = 'map/updatephototimor_form.html'
    model = PhotoTimor
    fields = ['image']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        target = self.kwargs['pk']
        context = super(UpdatePhotoViazenView, self).get_context_data(*args, **kwargs)
        context['journey_photos'] = PhotoTimor.objects.filter(id=target)
        return context


class ViazenUpdateView(UpdateView):
    template_name = 'map/viajen_form.html'
    model = IstoriaViazen
    fields = ['title', 'description', 'duration_of_trip']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['update_viazen'] = _("Update Journey History")

        return context

    def form_valid(self, form):

        for photo_file in self.request.FILES.getlist('photos'):
            photo = PhotoTimor.objects.create(istoriaviazen=self.object, image=photo_file)
            self.object.photos.add(photo)

        redirect = super().form_valid(form)

        return redirect


class ViazenDeleteView(DeleteView):
    model = IstoriaViazen
    success_url = reverse_lazy('home')


class DeletePhotoView(DeleteView):
    model = PhotoTimor
    template_name = 'map/istoriaviazen_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else self.success_url



class StyleGuideView(TemplateView):
    template_name = 'map/style_guide.html'
