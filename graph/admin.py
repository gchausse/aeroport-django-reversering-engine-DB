# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Airport)
admin.site.register(Baggage)
admin.site.register(Compagny)
admin.site.register(Crew)
admin.site.register(Flight)
admin.site.register(Passengers)
admin.site.register(Plane)