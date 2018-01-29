from django.contrib import admin
from .models import IoTDevice, Question, IoTMachine

# Register your models here.



class IoTDeviceModelAdmin(admin.ModelAdmin):

    list_display = ['device_name', 'device_id', 'updated_at']
    list_display_links = ['updated_at']
    list_editable = ['device_name']
    list_filter = ['device_name', 'updated_at']

    search_fields = ['device_id', 'device_owner']
    #ordering = ['device_id', 'slug', 'created_at']

    class Meta:
        model = IoTDevice
        fields = ('content')



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




admin.site.register(IoTDevice)
admin.site.register(Question)
admin.site.register(IoTMachine, IoTMachineAdmin)