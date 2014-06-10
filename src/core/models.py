# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class Subject(models.Model):
    name = models.CharField(max_length=30)

    def get_info(self):
        return {'name': self.name, 'pk': self.pk}

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    idnumber = models.IntegerField(null=True, blank=True, default=0)
    telephone = models.IntegerField(null=True, blank=True, default=0)
    cellphone = models.IntegerField(null=True, blank=True, default=0)

    def get_info(self):
        return {'name': self.get_full_name(),
                'username': self.username}

    def __unicode__(self):
        return self.get_full_name() or self.username


class JoinGroupRequest(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return u'%s %s' % (self.user.get_full_name(), self.group)


class SubjectGroup(models.Model):
    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)
    teacher = models.ForeignKey(User)
    hours = models.IntegerField(default=1)

    def get_info(self):
        return {
            'subject': self.subject.get_info(),
            'group': {
                'name': self.group.name,
                'pk': self.group.pk
            },
            'teacher': self.teacher.get_info()
        }

    def __unicode__(self):
        return u'%s %s' % (self.subject, self.group)
