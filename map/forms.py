from django.forms import ModelForm
from .models import Istoriaviazen


class IstoriaviazenForm(ModelForm):
    class Meta:
        model = Istoriaviazen
        fields = ['title', 'description', 'people']
