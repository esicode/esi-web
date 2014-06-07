from django.contrib import admin
from core.models import JoinGroupRequest
from core.models import Subject
from core.models import SubjectGroup
from core.models import User

admin.site.register(JoinGroupRequest)
admin.site.register(Subject)
admin.site.register(SubjectGroup)
admin.site.register(User)
