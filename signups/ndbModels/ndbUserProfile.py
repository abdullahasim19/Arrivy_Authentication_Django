from google.cloud import ndb
from signups.extraClasses import *
from .ndbUser import User
from .ndbCompanyProfile import CRMServiceInfo,OldExternalIntegration


class UserProfile(ndb.Model):
    owner = ndb.IntegerProperty()
    fullname = ndb.StringProperty()
    address = ndb.StringProperty()
    exact_location = ndb.GeoPtProperty()
    # we don't need to set any default value here as we are unsure about the state of old customers and
    # we can not assume any value for them
    is_address_geo_coded = ndb.BooleanProperty()
    country = ndb.StringProperty()
    phone1 = ndb.StringProperty()
    phone2 = ndb.StringProperty()
    support_email = ndb.StringProperty()
    intro = ndb.StringProperty()
    details = ndb.TextProperty()
    company_type = ndb.IntegerProperty(
        choices=[
            CompanyType.MOVING,
            CompanyType.DELIVERY,
            CompanyType.FOODDELIVERY,
            CompanyType.MAIDSERVICE,
            CompanyType.HOMECARE,
            CompanyType.SERVICE,
            CompanyType.OTHER,
            CompanyType.COMMERCIALSERVICES,
            CompanyType.CONSTRUCTIONS,
            CompanyType.DELIVERYLOGISTICS,
            CompanyType.EVENT,
            CompanyType.FIELDHEALTHCARE,
            CompanyType.FIELDSALES,
            CompanyType.HOMESERVICES,
            CompanyType.INSPECTIONS,
            CompanyType.INTERNETSERVICEPROVIDER,
            CompanyType.SECURITY,
            CompanyType.SOLAR,
            CompanyType.UTILITY,
            CompanyType.ROOFING],
        default=CompanyType.SERVICE)

    plan_id = ndb.IntegerProperty(default=PlanType.TEAM_MEMBERS)
    plan = ndb.StringProperty(default=convert_plan_type_to_text(PlanType.TEAM_MEMBERS))
    reminder_notification_time = ndb.IntegerProperty(default=0)
    reminder_notification_time_hours = ndb.IntegerProperty(default=DEFAULT_TASK_REMINDER_NOTIFICATION_TIME)
    emergency = ndb.StringProperty()
    image_id = ndb.IntegerProperty()
    image_path = ndb.StringProperty()
    website = ndb.StringProperty()
    social_links = ndb.JsonProperty()
    company_owned = ndb.BooleanProperty()
    company_entity_id = ndb.IntegerProperty()
    owned_company_id = ndb.IntegerProperty()
    default_entity_id = ndb.IntegerProperty()
    timezone = ndb.StringProperty()
    acquisition_source = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    trial_expiration_date = ndb.DateProperty()
    discount = ndb.IntegerProperty(default=0)
    additional_charges = ndb.JsonProperty()
    self_scheduling = ndb.BooleanProperty(default=False)

    enable_customer_task_confirmation = ndb.BooleanProperty(default=False)
    enable_late_and_no_show_notification = ndb.BooleanProperty(default=False)
    min_acceptable_rating = ndb.IntegerProperty(default=4)
    custom_webhook = ndb.StringProperty()
    custom_webhook_authentication_keys = ndb.JsonProperty()
    color = ndb.StringProperty()
    pending_review_reminder_attempts = ndb.IntegerProperty(default=DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS)
    ratings_fetch_URL = ndb.StringProperty()
    ratings_fetch_URL_authentication_keys = ndb.JsonProperty()
    ratings_fetch_URL_v2 = ndb.StringProperty()
    ratings_fetch_URL_v2_authentication_keys = ndb.JsonProperty()
    enable_team_confirmation = ndb.BooleanProperty(default=False)
    team_confirmation_time = ndb.TimeProperty()
    calender_start_time = ndb.TimeProperty()
    calender_end_time = ndb.TimeProperty()
    team_confirmation_time_zone = ndb.StringProperty()
    team_confirmation_day = ndb.IntegerProperty()
    team_confirmation_notification_type = ndb.StringProperty()
    team_confirmation_custom_message = ndb.StringProperty()

    team_confirmation_queued_task_name = ndb.StringProperty()
    rating_type = ndb.StringProperty(default=DEFAULT_RATING_TYPE)
    review_response_delay = ndb.IntegerProperty(default=DEFAULT_REVIEW_RESPONSE_DELAY)

    exceptions = ndb.JsonProperty()
    samsara_integration_info = ndb.StructuredProperty(OldExternalIntegration)
    task_notifications_settings = ndb.JsonProperty()
    status_priority = ndb.JsonProperty()
    mileage_unit = ndb.IntegerProperty()
    calendar_week_starts_from = ndb.StringProperty()
    calendar_week_ends_on = ndb.StringProperty()
    is_documents_disabled = ndb.BooleanProperty(default=True)
    filters = ndb.JsonProperty()
    time_line_filters = ndb.JsonProperty()
    can_field_crew_view_contact_info = ndb.BooleanProperty(default=True)
    reminder_time_after_task_creation = ndb.IntegerProperty(default=0)
    signup_channel = ndb.IntegerProperty(choices=[
        InvitationChannelType.EMAIL,
        InvitationChannelType.SMS,
        InvitationChannelType.USERNAME
    ], default=InvitationChannelType.EMAIL)
    signup_address = ndb.StringProperty(default=None)
    route_start = ndb.IntegerProperty(
        choices=[RouteStartPoint.GROUP,
                 RouteStartPoint.TASK],
        default=RouteStartPoint.GROUP
    )
    enable_route_editing = ndb.BooleanProperty(default=False)
    additional_addresses = ndb.JsonProperty()
    show_route_editing_instructions = ndb.BooleanProperty()
    auto_fill_customer_address = ndb.BooleanProperty(default=True)

    # Enterprise branding fields.
    show_brand_color = ndb.BooleanProperty(default=False)
    custom_message_template = ndb.StringProperty()
    email_domain = ndb.StringProperty()
    livetrack_base_url = ndb.StringProperty()
    default_email_sender = ndb.StringProperty()
    white_label_enabled = ndb.BooleanProperty(default=False)
    livetrack_company_name = ndb.StringProperty()

    enforce_group_company_timezone_on_customer_communication = ndb.BooleanProperty(default=False)
    enable_inventory = ndb.BooleanProperty(default=False)
    is_on_boarding_guide_visited = ndb.BooleanProperty(default=False)
    enable_customer_view_settings_for_scheduler = ndb.BooleanProperty(default=False)
    send_task_reminders_according_to_work_week_settings = ndb.BooleanProperty(default=True)

    enable_forms = ndb.BooleanProperty(default=False)
    crm_services_info = ndb.StructuredProperty(CRMServiceInfo, repeated=True)

    enable_safety_measures = ndb.BooleanProperty(default=False)
    safety_measures_title = ndb.StringProperty()
    safety_measures = ndb.TextProperty()
    default_time_interval = ndb.IntegerProperty(default=30)

    is_premium_enabled = ndb.BooleanProperty(default=False)
    # Example object: {"Route Editing": {"price": 250, "discount": 10}, "Forms": {"price": 100, "discount": 10}}
    premium_charges_details = ndb.JsonProperty()

    is_localization_enabled = ndb.BooleanProperty(default=False)



    def get_owner_key_urlsafe(self):
        key = ndb.Key(User, self.owner)
        return key.urlsafe()


