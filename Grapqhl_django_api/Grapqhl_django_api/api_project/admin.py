from django.contrib import admin

# Register your models here.
from .models import Film, People, Planet
admin.site.register(Film)
admin.site.register(People)
admin.site.register(Planet)
