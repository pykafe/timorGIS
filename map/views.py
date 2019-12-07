from django.shortcuts import render

from django.views.generic.base import TemplateView
from .models import Suco

class MapView(TemplateView):
    template_name = 'map/mapview.html'
    suco = Suco.objects.all()
    context = {'suco': suco}

    def get(self, request):
        return render(request, self.template_name, self.context)
