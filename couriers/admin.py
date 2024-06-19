from django.contrib import admin
from .models import Courier


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'middle_name',
                    'phone_number', 'password']
