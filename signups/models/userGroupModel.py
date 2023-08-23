from django.db import models
from .userModel import ArrivyUser

class Group(models.Model):
    owner = models.IntegerField()
    created_by = models.IntegerField()
    # Automatically add entity creation time
    created = models.DateTimeField(auto_now_add=True)
    # Automatically track entity update time
    updated = models.DateTimeField(auto_now=True)
    social_links = models.JSONField()
    name = models.CharField(blank=True,null=True,max_length=100)
    description = models.TextField()
    email = models.CharField(blank=True,null=True,max_length=100)
    phone = models.CharField(blank=True,null=True,max_length=100)
    mobile_number = models.CharField(blank=True,null=True,max_length=100)
    address_line_1 = models.CharField(blank=True,null=True,max_length=100)
    address_line_2 = models.CharField(blank=True,null=True,max_length=100)
    city = models.CharField(blank=True,null=True,max_length=100)
    state = models.CharField(blank=True,null=True,max_length=100)
    country = models.CharField(blank=True,null=True,max_length=100)
    zipcode = models.CharField(blank=True,null=True,max_length=100)
    exact_location = models.CharField(max_length=100,blank=True,null=True)
    use_lat_lng_address = models.BooleanField(default=False)
    complete_address = models.CharField(blank=True,null=True,max_length=100)
    # we don't need to set any default value here as we are unsure about the state of old customers and
    # we can not assume any value for them
    is_address_geo_coded = models.BooleanField()
    timezone = models.CharField(blank=True,null=True,max_length=100)
    emergency = models.CharField(blank=True,null=True,max_length=100)
    image_id = models.IntegerField(blank=True,null=True)
    image_path = models.CharField(blank=True,null=True,max_length=100)
    extra_fields = models.JSONField()
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    is_implicit = models.BooleanField(default=False)
    website = models.CharField(blank=True,null=True,max_length=100)
    additional_addresses = models.JSONField()
    default_locale = models.CharField(blank=True,null=True,max_length=100)
    locale_date_format = models.CharField(blank=True,null=True,max_length=100)
    locale_time_format = models.CharField(blank=True,null=True,max_length=100)
