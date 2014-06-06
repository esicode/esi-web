# -*- coding: utf-8 -*-

from django.db import models
from core.models import (SubjectGroup, User)


class PlaceType(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Place(models.Model):
    number = models.IntegerField()
    placetype = models.ForeignKey(PlaceType)

    def __unicode__(self):
        name = '%s %d' % (str(self.placetype),
                          int(self.number))
        return name.decode('utf-8')


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
        return u'%s %s %s' % (self.subjectgroup, self.date, self.start)


class Absence(models.Model):
    teacher = models.ForeignKey(User)
    start = models.DateTimeField()
    end = models.DateTimeField()
    message = models.CharField(max_length=200)
    visible = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s desde %s hasta %s' % (self.teacher,
                                          self.start.strftime(
                                              u'%d de %b de %Y (%l:%M%p)'),
                                          self.end.strftime(
                                              u'%d de %b de %Y (%l:%M%p)'))
