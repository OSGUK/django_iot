from django.contrib import admin
from .models import IoT_Device

# Register your models here.

class IoT_DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name','device_id','slug', 'local_ip')
    search_fields = ('device_id', 'sluc', 'device_owner')
    ordering = ('device_id','slug', 'created_at')

admin.site.register(IoT_Device, IoT_DeviceAdmin)
