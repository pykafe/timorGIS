from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import DateRangeField
from psycopg2.extras import DateRange


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
