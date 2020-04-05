from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Aldeia, Suco, District
from .models import Aldeia, Suco, Subdistrict, District, Point, PhotoTimor, Istoriaviazen
from PIL import Image
from map.get_image_location import get_exif_data, get_lat_lon
from map.forms import IstoriaviazenForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView



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
            get_data = get_exif_data(Image.open(photo.image.path))
            lat, lon = get_lat_lon(get_data)
            if lat and lon:
                images.append({"lat": lat, "lon": lon, "photo": photo.image.url})
        context['geoimages'] = images
        context['istoriaviazen'] = IstoriaviazenForm()
        return context


class AnotherView(TemplateView):
    template_name = 'map/another.html'


class HatamaViazenView(FormView):
    template_name = 'map/hatamaviazenview.html'
    form_class = IstoriaviazenForm
    success_url = reverse_lazy('home')


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image_trip')
        if form.is_valid():
            for f in files:
            # Do something with each file.
                return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ViazenUpdateView(UpdateView):
    model = Istoriaviazen
    fields = ['title', 'description', 'date', 'creator', 'image_trip']
    success_url = reverse_lazy('home')


class ViazenDeleteView(DeleteView):
    model = Istoriaviazen
    success_url = reverse_lazy('home')
