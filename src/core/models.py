# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

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
