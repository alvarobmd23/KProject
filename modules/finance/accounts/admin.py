from django.contrib import admin

from .models import Analitic, Sintetic, TypeAccount

admin.site.register(TypeAccount)
admin.site.register(Sintetic)
admin.site.register(Analitic)
