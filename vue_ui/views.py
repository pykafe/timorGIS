from django.conf import settings
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.http.response import HttpResponseForbidden
from django.views.generic.base import TemplateView, View
from django.urls import reverse
from django.core.cache import cache

from map.models import District, PhotoTimor, IstoriaViazen, CommentPhoto

class VueView(TemplateView):
    template_name = 'vue_ui/index.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'urls': dict(
                openstreetmap=settings.OPENSTREETMAP_URL,
                geojson=reverse("api_geojson"),
                images=reverse("api_images"),
                commentphoto=reverse("api_commentphoto"),
                istoriaviazen=reverse("api_istoriaviazen"),
                login=reverse("api_login"),
                add_journey=reverse("api_add_istoria"),
                media_url=settings.MEDIA_URL,
            )
        }
        return context

class AddIstoriaView(View):
    def post(self, request, *args, **kwargs):
        istoria = IstoriaViazen.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            duration_of_trip=(request.POST["fromDate"], request.POST["toDate"]),
            creator=request.user,
        )
        response_data = {
            "istoria": istoria.to_json(),
            "photos": [],
        }
        for photo_file in self.request.FILES.getlist('photos'):
            photo = PhotoTimor.objects.create(istoriaviazen=istoria, image=photo_file)
            response_data["photos"].append(photo.to_json())

        return JsonResponse(response_data)

def login_api(request):
    if request.user.is_authenticated:
        response = JsonResponse(
            {'name': request.user.get_full_name()
        })
    else:
        response = HttpResponse(status=401, reason="You need to login")
    return response

def geojson_api(request):
    geojson = cache.get('api_geojson')
    if geojson == None:
        geojson = serialize('geojson', District.objects.all(), geometry_field='geom')
        cache.set('api_geojson', geojson)
    response = HttpResponse(geojson, content_type="application/json")
    return response

def images_api(request):
    images = [
        p.to_json()
        for p in PhotoTimor.objects.all().select_related("istoriaviazen", "istoriaviazen__creator")
    ]
    response = JsonResponse(images, safe=False)
    return response

def istoriaviazen_api(request):
    viazen = [
        v.to_json()
        for v in IstoriaViazen.objects.all().select_related('creator')
    ]
    response = JsonResponse(viazen, safe=False)
    return response

def commentphoto_api(request):
    comment = [
        c.to_json()
        for c in CommentPhoto.objects.filter(is_public=True).select_related('user')
    ]
    response = JsonResponse(comment, safe=False)
    return response

