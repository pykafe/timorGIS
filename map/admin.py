from django.contrib.gis import admin
from .models import Suco, Aldeia, District, Subdistrict
from .models import Suco, Aldeia, District, Subdistrict, Point, PhotoTimor, Istoriaviazen
from leaflet.admin import LeafletGeoAdmin


class SucoAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'subdistrict_name', 'district_name']
    list_filter = ['district_name', 'subdistrict_name']


class AldeiaAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


class SubdistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Suco, SucoAdmin)
admin.site.register(Aldeia, AldeiaAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Subdistrict, SubdistrictAdmin)
admin.site.register(Istoriaviazen)
admin.site.register(
    Point,                      #<-- this is a model
    LeafletGeoAdmin,
    settings_overrides =  {
        'DEFAULT_CENTER': ([-8.8315139, 125.6199236,8]),
        'DEFAULT_ZOOM': 8,
    }
)
admin.site.register(PhotoTimor)
