from django.contrib import admin
from .models import Map


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_longitude', 'start_latitude', 'end_longitude',
                    'end_latitude', 'order']
