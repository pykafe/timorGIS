from django.contrib.gis.db import models


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
