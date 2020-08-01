from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.contrib.postgres.fields import DateRangeField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from psycopg2.extras import DateRange
from django.core.exceptions import ValidationError
from map.gps_images import ImageMetaData


class Suco(models.Model):
    name = models.CharField(max_length=124)
    district_name = models.CharField(max_length=124)
    subdistrict_name = models.CharField(max_length=124)

    geom = models.PolygonField()

    def __str__(self):
        return self.name


class Aldeia(models.Model):
    name = models.CharField(max_length=124)

    geom = models.PointField()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=124)

    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name


class Subdistrict(models.Model):
    name = models.CharField(max_length=124)

    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name


class IstoriaViazen(models.Model):
    title = models.CharField(max_length=80, null=False)
    description = models.TextField(null=False)
    duration_of_trip = DateRangeField()
    created_at = models.DateTimeField(null=False, blank=False, default=timezone.now)
    creator = models.ForeignKey(User, related_name='istoria', on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.pk}'


def queryobject(obj, point):
    queryset = obj.objects.filter(geom__contains=point)
    return queryset

class PhotoTimor(models.Model):
    istoriaviazen = models.ForeignKey(IstoriaViazen, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos', verbose_name='Timor Photo')
    created_at = models.DateTimeField(null=False, blank=False, default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{photo}".format(photo=self.image)

    def clean(self):
        """check image if it has longitude and latitude before upload to media file"""
        if self.image:
            try:
                get_data = ImageMetaData(self.image)
            except AttributeError:
                raise ValidationError(_("This image type does not support" ))

            lat, lon = get_data.get_lat_lng()
            if not lat and not lon:
                raise ValidationError(_("This image has no GPS details" ))


    def point(self):
        ''' return the point the photo was taken at if known'''
        try:
            get_data = ImageMetaData(self.image)
        except AttributeError:
            return None
        lat, lon = get_data.get_lat_lng()
        if lat and lon:
            return Point(lon, lat)
        return None

    def get_areas(self, model):
        if self.point():
            return queryobject(model, self.point())
        else:
            return model.objects.none()

    def sucos(self):
        ''' returns a queryset of all Sucos this photo intersects with '''
        return self.get_areas(Suco)

    def subdistricts(self):
        ''' returns a queryset of all Subdistricts this photo intersects with '''
        return self.get_areas(Subdistrict)

    def districts(self):
        ''' returns a queryset of all Districts this photo intersects with '''
        return self.get_areas(District)

    def suco(self):
        ''' return the suco the photo was taken in '''
        return ', '.join(self.get_areas(Suco).values_list('name', flat=True))

    def subdistrict(self):
        ''' return the subdistrict the photo was taken in '''
        return ', '.join(self.get_areas(Subdistrict).values_list('name', flat=True))

    def district(self):
        ''' return the district the photo was taken in '''
        return ', '.join(self.get_areas(District).values_list('name', flat=True))
