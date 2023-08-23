from google.cloud import ndb
from signups.extraClasses import *


class UserCompany(ndb.Model):
    owned_company_id = ndb.IntegerProperty()
    company_entity_id = ndb.IntegerProperty()
    is_disabled = ndb.BooleanProperty(default=False)
    signup_channel = ndb.IntegerProperty(choices=[
        InvitationChannelType.EMAIL,
        InvitationChannelType.SMS,
        InvitationChannelType.USERNAME
    ],default=InvitationChannelType.EMAIL)
    signup_address = ndb.StringProperty(default=None)
    # Used in migration when Entity has both email and phone as a auth_ids.
    signup_channel_2 = ndb.IntegerProperty(choices=[
        InvitationChannelType.EMAIL,
        InvitationChannelType.SMS,
        InvitationChannelType.USERNAME
    ],default=InvitationChannelType.EMAIL)
    signup_address_2 = ndb.StringProperty(default=None)

    #  todo: remove this flag after we ran migrations
    is_disable = ndb.BooleanProperty(default=False)

    # user type will differentiate between customer and crew
    user_type = ndb.IntegerProperty(
        choices=[
            EntityUserTypes.CUSTOMER,
            EntityUserTypes.CREW
        ],
        default=EntityUserTypes.CREW)


class EntityProfile(ndb.Model):
    owner = ndb.IntegerProperty()
    address = ndb.StringProperty()
    country = ndb.StringProperty()
    details = ndb.TextProperty()
    email = ndb.StringProperty()
    emergency = ndb.StringProperty()
    exact_location = ndb.GeoPtProperty()
    fullname = ndb.StringProperty()
    image_id = ndb.IntegerProperty()
    image_path = ndb.StringProperty()
    intro = ndb.StringProperty()

    acquisition_source = ndb.StringProperty()

    company_entity_id = ndb.IntegerProperty()
    owned_company_id = ndb.IntegerProperty()

    mobile_number = ndb.StringProperty()
    phone = ndb.StringProperty()
    social_links = ndb.JsonProperty()
    timezone = ndb.StringProperty()
    user_companies = ndb.StructuredProperty(UserCompany, repeated=True)
    is_on_boarding_guide_visited = ndb.BooleanProperty(default=False)

    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

