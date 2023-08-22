from django.contrib import admin

from .models import *

admin.site.register(Event)
admin.site.register(Instrument)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)

