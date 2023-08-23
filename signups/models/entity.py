from django.db import models
from .userModel import ArrivyUser
from signups.extraClasses import *


class Entity(models.Model):
    owner = models.ForeignKey(ArrivyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)
    extra_fields = models.JSONField(blank=True, null=True)
    is_default = models.BooleanField(default=False, blank=True, null=True)
    can_turnoff_location = models.BooleanField(default=True, blank=True, null=True)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    is_disabled = models.BooleanField(default=False, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    notifications = models.JSONField(blank=True, null=True)
    skill_ids = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_status_priority_notifications_disabled = models.BooleanField(default=False)
    invite_status = models.IntegerField(
        choices=[
            (EntityInviteStatus.PENDING, 'Pending'),
            (EntityInviteStatus.ACCEPTED, 'Accepted]')
        ],
        default=EntityInviteStatus.PENDING)

    joined_datetime = models.DateTimeField(blank=True, null=True)
    additional_group_ids = models.IntegerField(blank=True, null=True)
    allow_status_notifications = models.JSONField(blank=True, null=True)
    # Automatically add entity creation time
    created = models.DateTimeField(auto_now_add=True)
    # Automatically track entity update time
    updated = models.DateTimeField(auto_now=True)

    # to store source of external platform sources from which tasks are fetched using data fetch module
    external_type = models.CharField(max_length=100, blank=True, null=True)

    # this is a temporary flag which will be used with schedulers only to indicate if a specific scheduler can see
    # customers of all groups or of his own group only.
    # TODO: This flag should be be removed after we have done the CUSTOM PERMISSIONS feature.
    can_view_customers_of_all_groups = models.BooleanField(default=True)

    # To keep track of the LATEST task where the entity is clocked in. Entity can be clocked in on task at a time
    # and this attr will indicate what task is this
    active_task_id = models.IntegerField(blank=True, null=True)

    # To limit users to be able to login in kiosk mode only
    allow_login_in_kiosk_mode_only = models.BooleanField(default=False)

    # To indicate if an entity should be included in billing or not. This flag will work independently
    # of permission role of the entity. The only exception for now is that LIMITED ACCESS role is FREE
    # irrespective of this flag.
    is_included_in_billing = models.BooleanField(default=True)

    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    exact_location = models.CharField(max_length=100, blank=True, null=True)
    use_lat_lng_address = models.BooleanField(default=False)
    complete_address = models.CharField(max_length=100, blank=True, null=True)
    is_address_geo_coded = models.BooleanField(blank=True, null=True)
    # user type will differentiate between customer and crew
    user_type = models.IntegerField(
        choices=[
            (EntityUserTypes.CUSTOMER, "Customer"),
            (EntityUserTypes.CREW, "Crew")
        ],
        default=EntityUserTypes.CREW, blank=True, null=True
    )

    # Will add against customer for which entity is created
    entity_customer_id = models.IntegerField(blank=True, null=True)
    # Company bookings which are visible to customer on company customer portal
    visible_bookings = models.IntegerField(blank=True, null=True)

    given = ['owner', 'name']
    okta_user_id = models.CharField(max_length=100, blank=True, null=True)
