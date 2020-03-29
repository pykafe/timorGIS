from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import DateRangeField
from psycopg2.extras import DateRange
from map.get_image_location import get_exif_data, get_lat_lon
from django.core.exceptions import ValidationError
from PIL import Image


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
    upload_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, related_name='istoria', on_delete=models.CASCADE)
    people = models.ManyToManyField(User, related_name='subistoria')

    def __str__(self):
        return f'{self.tite}, {self.pk}'


class Point(models.Model):
    name = models.CharField(max_length=100, blank=False)

    geom = models.PointField()

    description = models.TextField()

    def __str__(self):
        return '{} '.format(self.name)


class PhotoTimor(models.Model):
    image = models.ImageField(upload_to='photos', verbose_name='Timor Photo')


    def __str__(self):
        return "{photo}".format(photo=self.image)

    def clean(self):
        """check image if it has longitude and latitude before upload to media file"""
        if self.image:
            get_data = get_exif_data(Image.open(self.image))
            lat, lon = get_lat_lon(get_data)
            if not lat and not lon:
                raise ValidationError("This image don't have latitude and longitude" )
