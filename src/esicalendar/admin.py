from django.contrib import admin
from esicalendar.models import Place
from esicalendar.models import PlaceType
from esicalendar.models import Subject
from esicalendar.models import SubjectGroup
from esicalendar.models import User
from esicalendar.models import Event
from esicalendar.models import Absence

admin.site.register(Place)
admin.site.register(PlaceType)
admin.site.register(Subject)
admin.site.register(SubjectGroup)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Absence)
