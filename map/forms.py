from django.forms import ModelForm
from map.models  import Istoriaviazen
from django import forms


class IstoriaviazenForm(ModelForm):
    image_trip = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Istoriaviazen
        fields = ['title', 'description','date']
