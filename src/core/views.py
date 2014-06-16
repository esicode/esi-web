# -*- coding: utf-8 -*-
import json

# from django.shortcuts import render
from django import http

from django.views.generic.base import View
from django.views.generic import TemplateView

from django.contrib.auth.models import Group
from core.models import SubjectGroup
from core.models import User


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps(context)

    def api_get(self, *args, **kwargs):
        raise NotImplementedError()

    def api_post(self, *args, **kwargs):
        raise NotImplementedError()

    def get(self, *args, **kwargs):
        return self.render_to_response(self.api_get(*args, **kwargs))

    def post(self, *args, **kwargs):
        return self.render_to_response(self.api_post(*args, **kwargs))


class GroupAPIView(JSONResponseMixin, View):
    def api_get(self, context, pk):
        group = Group.objects.get(pk=pk)
        return {
            'name': group.name,
            'members': [
                {'name': user.get_full_name(), 'username': user.username}
                for user in User.objects.filter(groups=group)
            ]
        }


class GroupSubjectsAPIView(JSONResponseMixin, View):
    def api_get(self, context, pk):
        group = Group.objects.get(pk=pk)
        return [
            subjectgroup.get_info()
            for subjectgroup in SubjectGroup.objects.filter(group=group)
        ]


class GroupListAPIView(JSONResponseMixin, View):
    def api_get(self, context):
        groups = [{'name': group.name, 'pk': group.pk,
                   'members': len(User.objects.filter(groups=group))}
                  for group in Group.objects.all()]
        return groups


class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(TemplateView):
    template_name = "signup.html"


class UserAPIView(JSONResponseMixin, View):
    def api_get(self, context, username):
        user = User.objects.get(username=username)
        return {
            'full_name': user.get_full_name(),
            'first_name': user.first_name,
            'last_name': user.last_name,
            'short_name': user.get_short_name()
        }


class UserGroupsAPIView(JSONResponseMixin, View):
    def api_get(self, context, username):
        user = User.objects.get(username=username)
        return self.render_to_response({
            'student': [
                {'name': group.name, 'pk': group.pk}
                for group in user.groups.all()
            ],
            'teacher': [{'group': subjectgroup.group.pk,
                         'subject': subjectgroup.subject.name}
                        for subjectgroup in
                        SubjectGroup.objects.filter(teacher=user)]
        })


class UserPrivateAPIView(JSONResponseMixin, View):
    def api_get(self, context, username):
        user = User.objects.get(username=username)
        return self.render_to_response({
            'idnumber': user.idnumber,
            'telephone': user.telephone,
            'cellphone': user.cellphone,
            'email': user.email
        })


class SignUpAPIView(JSONResponseMixin, View):
    def validate(self, context):
        return {
            'user': True,
            'email': True,
            'firstname': True
        }

    def save(self, context):
        User.objects.create_user(self.request.POST['user'],
                                 self.request.POST['email'],
                                 first_name=self.request.POST['firstname'],
                                 last_name=self.request.POST['lastname'],
                                 password=self.request.POST['password1'],
                                 idnumber=self.request.POST['idnumber'],
                                 telephone=self.request.POST['telephone'],
                                 cellphone=self.request.POST['cellphone'])

    def api_post(self, context):
        validation = self.validate(context)
        if reduce(lambda x, y: x and validation[y], validation, True):
            self.save(context)
        return validation
