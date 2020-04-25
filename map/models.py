from django.contrib.gis.db import models
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
        return '{} pk:{}'.format(self.name, self.pk)


class Aldeia(models.Model):
    name = models.CharField(max_length=124)

    geom = models.PointField()

    def __str__(self):
        return '{} pk:{}'.format(self.name, self.pk)


class District(models.Model):
    name = models.CharField(max_length=124)

    geom = models.MultiPolygonField()

    def __str__(self):
        return '{} pk:{}'.format(self.name, self.pk)


class Subdistrict(models.Model):
    name = models.CharField(max_length=124)

    geom = models.MultiPolygonField()

    def __str__(self):
        return '{} pk:{}'.format(self.name, self.pk)


class Istoriaviazen(models.Model):
    title = models.CharField(max_length=80, null=False)
    description = models.TextField(null=False)
    date = DateRangeField()
    upload_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    creator = models.ForeignKey(User, related_name='istoria', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.pk}'


class PhotoTimor(models.Model):
    istoriaviazen = models.ForeignKey(Istoriaviazen, related_name='istoriaviazen', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos', verbose_name='Timor Photo')


    def __str__(self):
        return "{photo}".format(photo=self.image)

    def clean(self):
        """check image if it has longitude and latitude before upload to media file"""
        if self.image:
            try:
                get_data = ImageMetaData(self.image)
            except AttributeError:
                raise ValidationError("La simu imajen ho tipu gif" )

            lat, lon = get_data.get_lat_lng()
            if not lat and not lon:
                raise ValidationError("Imajen nee laiha detailhu GPS" )
