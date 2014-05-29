from django.db import models
from django.contrib.auth.models import AbstractUser


class PlaceType(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Place(models.Model):
    number = models.IntegerField()
    placetype = models.ForeignKey(PlaceType)

    def __unicode__(self):
        return '%s %d' % (self.placetype, self.number)


class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    idnumber = models.IntegerField(null=True, blank=True, default=0)
#    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.get_full_name()
