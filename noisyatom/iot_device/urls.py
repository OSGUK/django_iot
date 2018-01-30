from django.conf.urls import url
from django.contrib import admin


from .views import(
        iot_machines_register,
        iot_machine_find,

)


urlpatterns = [
    url(r'^register/$', iot_machines_register),
    url(r'^machine/(?P<mac_address>[0-9]+)/$', iot_machine_find),
]