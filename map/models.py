from django.contrib.gis.db import models


class Suco(models.Model):
    name = models.CharField(max_length=124)
    district_name = models.CharField(max_length=124)
    subdistrict_name = models.CharField(max_length=124)

    geom = models.PolygonField()

    def __str__(self):
        return '{} pk:{}'.format(self.name, self.pk)


class District(models.Model):
    name = models.CharField(max_length=124)

    geom = models.PolygonField()

    def __str__(self):
        return '{} pk:{}'.format(self.name, self.pk)