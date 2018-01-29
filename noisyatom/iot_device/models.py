from django.db import models
from account.models import Company

#from catalog.models import Category
from pygments.lexers import get_all_lexers              # A serializer library to allow us to serialize our DB objects
from pygments.styles import get_all_styles              # which will be used for our REST interface
from django.core.urlresolvers import reverse
from django.utils import timezone

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# A simple SQL structure to store the registration of an IoT Device. Most parameters are optional. The only mandatory
# part is the local IP address and the MAC address of the device. The MAC address is unique. The local IP address is
# a way to find this device in your local network for interacting with it. This is not meant to be a server which
# pushes and pulls data between the user and the device. This is more like a location register


class IoTMachine(models.Model):
    device_name = models.CharField(max_length=50, help_text='A human readable name for the device.')
    device_id = models.CharField(max_length=18, help_text='The MAC address of the device e.g. a0:c5:89:61:0c:24. This value must be unique to the system', unique=True)
    device_owner = models.EmailField(max_length=255, help_text='The email of the owner. Optional field', null=True, blank=True)
    local_ip = models.GenericIPAddressField(default="0.0.0.0", help_text='The current local IP of the device')
    multicast_address = models.CharField(max_length=255, default="raspberypi.local", help_text="This is the multicast DNS name of the device within it's local domain")
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name. Created by system on registration', null=True, blank=True)
    power = models.BigIntegerField(help_text='The normal power consumption of the device when working', default=0, null=True)
    device_ledger_url = models.URLField(max_length=500, help_text='The URL to access the W3C Open Ledger address for this device. Optional parameter', null=True, blank=True)
    bluetooth_address = models.CharField(max_length=6, help_text='The Blue Tooth address (BD_ADDR). A 48bit 6octet device identifier. Optional parameter', null=True, blank=True)
    long = models.DecimalField(max_digits=8, decimal_places=6, help_text='The latitude of the device up to a resolution of 10cm', default=0, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, help_text='The longitude of the device up to a resolution of 10cm', default=0, null=True)
    is_active = models.BooleanField(default=True)
    company_name = models.ForeignKey(Company, help_text="The company who own this IoT device. Optional parameter.", null=True, blank=True)
    description = models.TextField(help_text='A description of this device. What it does. How it works. Optional parameter', null=True, blank=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag. Optional parameter', null=True, blank=True)
    meta_description = models.CharField(max_length=255, help_text='Content for description of meta tag. Optional parameter', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_id

    class Meta:
        db_table = 'Internet of Things Machine'
        ordering = ['-created_at']
        verbose_name_plural = 'IoT Machines'

