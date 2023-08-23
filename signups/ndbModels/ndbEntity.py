from google.cloud import ndb
from signups.extraClasses import *

class Entity:
    owner = ndb.IntegerProperty()
    name = ndb.StringProperty()
    username = ndb.StringProperty()
    type = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
    color = ndb.StringProperty()
    details = ndb.StringProperty(compressed=True, indexed=False)
    image_id = ndb.IntegerProperty()
    image_path = ndb.StringProperty()
    extra_fields = ndb.JsonProperty()
    is_default = ndb.BooleanProperty(default=False)
    can_turnoff_location = ndb.BooleanProperty(default=True)
    external_id = ndb.StringProperty()
    is_disabled = ndb.BooleanProperty(default=False)
    group_id = ndb.IntegerProperty()
    notifications = ndb.JsonProperty()
    skill_ids = ndb.IntegerProperty(repeated=True)
    is_active = ndb.BooleanProperty(default=True)
    is_status_priority_notifications_disabled = ndb.BooleanProperty(default=False)

    invite_status = ndb.IntegerProperty(
        choices=[
            EntityInviteStatus.PENDING,
            EntityInviteStatus.ACCEPTED
        ],
        default=EntityInviteStatus.PENDING)

    joined_datetime = ndb.DateTimeProperty()
    additional_group_ids = ndb.IntegerProperty(repeated=True)
    allow_status_notifications = ndb.JsonProperty()

    # Automatically add entity creation time
    created = ndb.DateTimeProperty(auto_now_add=True)
    # Automatically track entity update time
    updated = ndb.DateTimeProperty(auto_now=True)

    # to store source of external platform sources from which tasks are fetched using data fetch module
    external_type = ndb.StringProperty()

    # this is a temporary flag which will be used with schedulers only to indicate if a specific scheduler can see
    # customers of all groups or of his own group only.
    # TODO: This flag should be be removed after we have done the CUSTOM PERMISSIONS feature.
    can_view_customers_of_all_groups = ndb.BooleanProperty(default=True)

    # To keep track of the LATEST task where the entity is clocked in. Entity can be clocked in on task at a time
    # and this attr will indicate what task is this
    active_task_id = ndb.IntegerProperty()

    # To limit users to be able to login in kiosk mode only
    allow_login_in_kiosk_mode_only = ndb.BooleanProperty(default=False)

    # To indicate if an entity should be included in billing or not. This flag will work independently
    # of permission role of the entity. The only exception for now is that LIMITED ACCESS role is FREE
    # irrespective of this flag.
    is_included_in_billing = ndb.BooleanProperty(default=True)

    address_line_1 = ndb.StringProperty()
    address_line_2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    country = ndb.StringProperty()
    zipcode = ndb.StringProperty()
    exact_location = ndb.GeoPtProperty()
    use_lat_lng_address = ndb.BooleanProperty(default=False)
    complete_address = ndb.StringProperty()
    is_address_geo_coded = ndb.BooleanProperty()
    # user type will differentiate between customer and crew
    user_type = ndb.IntegerProperty(
        choices=[
            EntityUserTypes.CUSTOMER,
            EntityUserTypes.CREW
        ],
        default=EntityUserTypes.CREW
    )

    # Will add against customer for which entity is created
    entity_customer_id = ndb.IntegerProperty()
    # Company bookings which are visible to customer on company customer portal
    visible_bookings = ndb.IntegerProperty(repeated=True)
