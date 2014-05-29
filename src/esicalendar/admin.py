from django.contrib import admin
from esicalendar.models import Place
from esicalendar.models import PlaceType
from esicalendar.models import Subject
from esicalendar.models import User

admin.site.register(Place)
admin.site.register(PlaceType)
admin.site.register(Subject)
admin.site.register(User)
