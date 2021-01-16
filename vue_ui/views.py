from django.views.generic.base import TemplateView


class VueView(TemplateView):
    template_name = 'vue_ui/index.html'