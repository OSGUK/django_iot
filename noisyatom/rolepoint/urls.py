from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from rolepoint.views import rolepoint_view, rolepoint_search


urlpatterns = [
    url('^$', rolepoint_view, name='rolepoint'),
    url('^search_page/$', rolepoint_search, name='rolepoint_search')
    # url('^dashboard/$', dashboard_view, name='admin_page'),
]
