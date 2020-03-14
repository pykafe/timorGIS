from django.forms import ModelForm
from map.models  import Istoriaviazen


class IstoriaviazenForm(ModelForm):
    class Meta:
        model = Istoriaviazen
        fields = ['title', 'description','date','people']
