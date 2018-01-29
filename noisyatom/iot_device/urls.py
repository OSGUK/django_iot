from django.conf.urls import url
from django.contrib import admin


from .views import(
        iot_machines_list,
        iot_machine_find,

)


urlpatterns = [
    url(r'^register/$', iot_machines_list),
    url(r'^machine/(?P<mac_address>[0-9]+)/$', iot_machine_find),
]