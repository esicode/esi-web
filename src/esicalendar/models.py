# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


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
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.get_full_name()


class SubjectGroup(models.Model):
    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)
    teacher = models.ForeignKey(User)
    hours = models.IntegerField(default=1)

    def __unicode__(self):
        return '%s %s' % (self.subject, self.group)


class Event(models.Model):
    subjectgroup = models.ForeignKey(SubjectGroup)
    place = models.ForeignKey(Place)
    start = models.TimeField()
    hours = models.IntegerField(default=1)
    date = models.CharField(max_length=3,
                            choices=(
                                ('SAT', 'Sábado'),
                                ('MON', 'Lunes'),
                                ('TUE', 'Martes'),
                                ('WED', 'Miércoles'),
                                ('THU', 'Jueves'),
                                ('FRI', 'Viernes')
                            ))

    def __unicode__(self):
        return '%s %s %s' % (self.subjectgroup, self.date, self.start)
