from django.contrib.gis import admin
from .models import Suco


class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']

admin.site.register(Suco, SucoAdmin)

