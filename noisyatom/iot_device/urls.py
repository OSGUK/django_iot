from django.conf.urls import url
from django.contrib import admin


from .views import(
        iot_machines_register,
        iot_machine_find,

)


urlpatterns = [
    url(r'^register/$', iot_machines_register),
    url(r'^machine/(?P<mac_address>[\w:\s]+)/$', iot_machine_find),
    #url(r"^machine/(?P<mac>([0-9A-F]{2}[:-]){5}([0-9A-F]{2}))", iot_machine_find2),
]