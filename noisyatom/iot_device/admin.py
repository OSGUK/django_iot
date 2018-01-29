from django.contrib import admin
from .models import IoTMachine

# Register your models here.

class IoTMachineAdmin(admin.ModelAdmin):

    list_display = ['device_name', 'device_id', 'device_owner']
    list_display_links = ['device_id']
    list_editable = ['device_name']
    list_filter = ['device_name', 'device_id']

    search_fields = ['device_id', 'device_owner']
    #ordering = ['device_id', 'slug', 'created_at']

    class Meta:
        model = IoTMachine
        fields = ('content')

admin.site.register(IoTMachine, IoTMachineAdmin)