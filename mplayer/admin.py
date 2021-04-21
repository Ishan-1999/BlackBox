from django.contrib import admin
from .models import Song

# Register your models here.
admin.site.site_header = 'BlackBox Administration'

admin.site.register(Song)