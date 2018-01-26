from django.db import models

# Create your models here.



class IoT_Device(models.Model):
    device_name = models.CharField(max_length=50, help_text='A human readable name for the device.')
    device_id = models.CharField(max_length=6, help_text='The MAC address of the device', unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    power = models.BigIntegerField(min=0, help_text='The normal power consumption of the device when working')
    device_owner = models.EmailField(max_length=255, help_text='The email of the owner')
    local_ip = models.IPAddressField(default="0.0.0.0", help_text='The current local IP of the device')
    multicast_address = models.CharField(max_length=255, default="raspberypi.local", help_text="This is the multicast DNS name of the device within it's local domain")
    two_d_bar_code = models.OneToOneField(
        QRcode,
        on_delete=models.CASCADE,
        primary_key=True,
        null=False,
        blank=True,
        default=0,
    )
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    company_name = models.ForeignKey(Company, null=True)
    description = models.TextField()
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description of meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'Internet of Things Device'
        ordering = ['-created_at']
        verbose_name_plural = 'Internet of Things Devices'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'catalog_product', (), {'product_slug': self.slug}

