from google.cloud import ndb
from signups.extraClasses import *


class KioskConfiguration(ndb.Model):
    allow_kiosk_mode = ndb.BooleanProperty(default=False)
    username_prefix = ndb.StringProperty()
    auto_logout_after = ndb.IntegerProperty(default=5)  # in seconds
    show_team_notification = ndb.BooleanProperty(default=True)
    show_assigned_entities_on_task = ndb.BooleanProperty(default=True)
    show_map = ndb.BooleanProperty(default=True)
    show_task_latest_status = ndb.BooleanProperty(default=True)
    show_customer_contact_options = ndb.BooleanProperty(default=True)

    def serialize(self):
        return dict(
            allow_kiosk_mode=self.allow_kiosk_mode,
            username_prefix=self.username_prefix,
            auto_logout_after=self.auto_logout_after,
            show_team_notification=self.show_team_notification,
            show_assigned_entities_on_task=self.show_assigned_entities_on_task,
            show_map=self.show_map,
            show_task_latest_status=self.show_task_latest_status,
            show_customer_contact_options=self.show_customer_contact_options if hasattr(self,
                                                                                        'show_customer_contact_options') else True,
        )


class CustomIntegrationInfo(ndb.Model):
    integration_type = ndb.IntegerProperty()


class CRMServiceInfo(ndb.Model):
    crm_type = ndb.IntegerProperty(
        choices=[
            ExternalIntegrationType.PIPEDRIVE
        ])
    crm_id = ndb.IntegerProperty()  # deal_id of pipe_drive


class OldExternalIntegration(ndb.Model):
    samsara_access_token = ndb.StringProperty()
    samsara_group_ids = ndb.IntegerProperty(repeated=True)


class QrSettingsInfo(ndb.Model):
    mode = ndb.IntegerProperty(
        choices=[QRSettingsModesTypes.AUTO, QRSettingsModesTypes.MANUAL, QRSettingsModesTypes.MIGRATION,
                 QRSettingsModesTypes.NO_MODE],
        default=QRSettingsModesTypes.AUTO)

    updated_at = ndb.DateTimeProperty(auto_now=True)
    updated_by = ndb.IntegerProperty()
    updated_by_user = ndb.StringProperty()


class CompanyProfile(ndb.Model):
    owner = ndb.IntegerProperty()
    fullname = ndb.StringProperty()
    address = ndb.StringProperty()
    exact_location = ndb.GeoPtProperty()
    # we don't need to set any default value here as we are unsure about the state of old customers and
    # we can not assume any value for them
    is_address_geo_coded = ndb.BooleanProperty()
    country = ndb.StringProperty()
    mobile_number = ndb.StringProperty()
    phone = ndb.StringProperty()
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
    team_reminder_queued_task_name = ndb.StringProperty()
    emergency = ndb.StringProperty()
    image_id = ndb.IntegerProperty()
    image_path = ndb.StringProperty()
    website = ndb.StringProperty()
    social_links = ndb.JsonProperty()
    default_entity_id = ndb.IntegerProperty()
    timezone = ndb.StringProperty()
    acquisition_source = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    trial_expiration_date = ndb.DateProperty()
    discount = ndb.IntegerProperty(default=0)
    additional_charges = ndb.JsonProperty()
    time_reporting_permissions = ndb.JsonProperty()
    short_day_format = ndb.BooleanProperty(default=False)
    full_day_format = ndb.BooleanProperty(default=False)

    enable_customer_task_confirmation = ndb.BooleanProperty(default=False)
    enable_late_and_no_show_notification = ndb.BooleanProperty(default=False)
    mark_task_late_when = ndb.StringProperty(default="one_assignee_is_late")
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
    team_confirmation_type = ndb.IntegerProperty(choices=[
        TeamConfirmationType.SCHEDULE,
        TeamConfirmationType.INSTANT],
        default=TeamConfirmationType.SCHEDULE)
    team_confirmation_custom_message = ndb.StringProperty()
    # change_reschedule_status_title is not using anymore
    change_reschedule_status_title = ndb.BooleanProperty(default=False)
    team_confirmation_queued_task_name = ndb.StringProperty()
    rating_type = ndb.StringProperty(default=DEFAULT_RATING_TYPE)
    rating_threshold = ndb.IntegerProperty()
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
    signup_channel = ndb.IntegerProperty(choices=[
        InvitationChannelType.EMAIL,
        InvitationChannelType.SMS,
        InvitationChannelType.USERNAME
    ],
        default=InvitationChannelType.EMAIL)
    signup_address = ndb.StringProperty(default=None)
    can_field_crew_view_contact_info = ndb.BooleanProperty(default=True)
    reminder_time_after_task_creation = ndb.IntegerProperty(default=0)
    route_start = ndb.IntegerProperty(
        choices=[RouteStartPoint.GROUP,
                 RouteStartPoint.TASK],
        default=RouteStartPoint.GROUP
    )
    depot_departure_time = ndb.TimeProperty()
    additional_addresses = ndb.JsonProperty()
    show_route_editing_instructions = ndb.BooleanProperty(default=True)
    auto_fill_customer_address = ndb.BooleanProperty(default=True)
    can_customer_mark_statuses = ndb.BooleanProperty(default=False)

    # Enterprise branding fields.
    show_brand_color = ndb.BooleanProperty(default=False)
    custom_message_template = ndb.StringProperty()
    email_domain = ndb.StringProperty()
    livetrack_base_url = ndb.StringProperty()
    default_email_sender = ndb.StringProperty()
    livetrack_company_name = ndb.StringProperty()
    email_sender = ndb.StringProperty()
    sender_name = ndb.StringProperty()

    # TODO: we need to move the above enterprise branding fields inside these JSON property
    white_labeling_settings = ndb.JsonProperty()  # This should always hold authentication keys of third party platforms like Twilio and should never be exposed publicily
    white_labeling_public_settings = ndb.JsonProperty()
    white_label_enabled = ndb.BooleanProperty(default=False)

    enforce_group_company_timezone_on_customer_communication = ndb.BooleanProperty(default=False)
    enable_inventory = ndb.BooleanProperty(default=False)
    is_on_boarding_guide_visited = ndb.BooleanProperty(default=False)
    self_scheduling = ndb.BooleanProperty(default=False)
    enable_customer_view_settings_for_scheduler = ndb.BooleanProperty(default=False)
    send_task_reminders_according_to_work_week_settings = ndb.BooleanProperty(default=True)

    crm_services_info = ndb.StructuredProperty(CRMServiceInfo, repeated=True)

    enable_safety_measures = ndb.BooleanProperty(default=False)
    safety_measures_title = ndb.StringProperty()
    safety_measures = ndb.TextProperty()
    default_time_interval = ndb.IntegerProperty(default=30)

    is_localization_enabled = ndb.BooleanProperty(default=False)
    show_time_zone_name_in_notifications = ndb.BooleanProperty(default=False)
    use_company_or_group_time_zone_for_internal_notifications = ndb.BooleanProperty(default=False)
    show_social_links_on_live_track = ndb.BooleanProperty(default=True)

    ui_filters_settings = ndb.JsonProperty()

    enable_multi_day = ndb.BooleanProperty(default=True)

    # This flag has been retired and should NEVER be used
    auto_clock_out_on_complete = ndb.BooleanProperty(default=False)

    default_locale = ndb.StringProperty()
    locale_date_format = ndb.StringProperty()
    locale_time_format = ndb.StringProperty()
    show_directions_on_live_track = ndb.BooleanProperty(default=True)

    enable_pdf_stitching = ndb.BooleanProperty(default=False)
    enable_pdf_annotations = ndb.BooleanProperty(default=False)
    form_pdf_scale_ios = ndb.FloatProperty(default=.75)
    form_pdf_scale_web = ndb.FloatProperty(default=1.5)

    # TODO: we need the default value as True after the proper feature release
    enable_time_reporting = ndb.BooleanProperty(default=False)

    # Attributes to be used in Kiosk mode
    allow_kiosk_mode = ndb.BooleanProperty(default=False)
    username_prefix = ndb.StringProperty()
    auto_logout_after = ndb.IntegerProperty()  # in seconds

    enable_sms_notifications = ndb.BooleanProperty(default=False)
    # enable_status_priority_sms_notifications is deprecated
    enable_status_priority_sms_notifications = ndb.BooleanProperty(default=False)

    can_create_booking_only = ndb.BooleanProperty(default=False)

    kiosk_configuration = ndb.StructuredProperty(KioskConfiguration)

    # Flag to trigger Form Auto Save
    auto_save_form = ndb.BooleanProperty(default=False)

    # Flag to decide whether to apply filters on unscheduled bucket or not
    apply_filters_on_unscheduled_bucket = ndb.BooleanProperty(default=False)

    # Flag to decide whether to open task or activity form on tasks views
    choose_between_activity_or_tasks = ndb.BooleanProperty(default=False)

    # Flag to decide whether to show tasks scheduled confirmation modal
    do_not_show_tasks_scheduled_modal = ndb.BooleanProperty(default=False)

    # To control crew availability feature
    enable_crew_availability = ndb.BooleanProperty(default=False)
    allow_auto_approval_of_crew_availability_requests = ndb.BooleanProperty(default=True)
    permission_groups_that_can_approve_crew_availability_requests = ndb.StringProperty(repeated=True)

    # To control recurring tasks feature
    enable_recurring_tasks = ndb.BooleanProperty(default=False)

    # For sending task create webhook when a booking task is rescheduled.
    send_task_create_webhook_on_booking_reschedule = ndb.BooleanProperty(default=False)

    # For Sending company_support an email whenever some integration sync is failed
    send_email_on_sync_fail = ndb.BooleanProperty(default=False)
    # enable API permissions for specific companies
    is_api_enabled = ndb.BooleanProperty(default=False)
    # Used for MY PORTER to hide reviews tab.
    show_reviews_to_viewer = ndb.BooleanProperty(default=True)
    # To control high density route planning feature
    enable_high_density_route_planning = ndb.BooleanProperty(default=False)
    # To control customer template custom section
    enable_customer_templates_custom_section = ndb.BooleanProperty(default=False)
    # To enable dock scheduling feature
    enable_dock_scheduling = ndb.BooleanProperty(default=False)

    # To skip form filling step in forms
    skip_form_filling_step = ndb.BooleanProperty(default=False)

    # To control time constraints in booking calendar
    enable_travel_time_constraint_on_booking = ndb.BooleanProperty(default=False)

    # To control customer portal feature
    enable_customer_portal = ndb.BooleanProperty(default=False)
    customer_portal_domain_name = ndb.StringProperty()

    # To control Elastic search feature
    enable_elastic_search = ndb.BooleanProperty(default=False)
    # To enable image compression on File uploads(i.e imageUpload Component)
    enable_image_compression = ndb.BooleanProperty(default=True)
    "--------------------------------- Custom Integrations Configurations --------------------------------------"
    custom_integrations = ndb.StructuredProperty(CustomIntegrationInfo, repeated=True)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------- Premium features control flags and billing attributes ---------------------------"
    # Any addition in the feature control flags should also be made in "get_premium_features_attribute_names" function
    enable_route_editing = ndb.BooleanProperty(default=False)
    enable_forms = ndb.BooleanProperty(default=False)
    enable_booking_schedule = ndb.BooleanProperty(default=False)
    enable_map_view = ndb.BooleanProperty(default=False)

    is_premium_enabled = ndb.BooleanProperty(default=False)

    # Example object: {"Route Editing": {"price": 250, "discount": 10}, "Forms": {"price": 100, "discount": 10}}
    premium_charges_details = ndb.JsonProperty()

    # When is plan is changed from Premium to Standard, we still need to provide premium features to the company till
    # next charge and also charge them as premium customer. This attr will hold the info that the plan of the company
    # need to be changed to Standard on the billing day.
    change_plan_to = ndb.StringProperty()
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ Analytics Attributes -------------------------------------------"
    # When business was contact for the first time
    contact_date = ndb.DateTimeProperty()

    # when businesses subscribe
    subscribe_date = ndb.DateTimeProperty()

    # when businesses unsubscribe
    tombstone_date = ndb.DateTimeProperty()

    # indicates businesses crm status
    crm_status = ndb.StringProperty(default="LEAD")

    # indicates business crm type
    crm_business_type = ndb.StringProperty(default="INTEGRATED")

    # indicates the business industry
    crm_business_industry = ndb.StringProperty(default="SERVICE")

    # when on-boarding of a business started
    onboarding_date = ndb.DateTimeProperty()

    # indicates the number of team members for company
    company_size = ndb.StringProperty()

    # indicates the list of features which are to be used by the company
    features = ndb.StringProperty()

    # indicates the list of internal integrations which are used by the company
    internal_integrated_softwares = ndb.StringProperty()

    # indicates the list of external integrations which are used by the company
    external_integrated_softwares = ndb.StringProperty()

    # indicates the onboarding details provided by the company
    onboarding_details = ndb.StringProperty()

    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ Account Verification Attributes --------------------------------"
    # Indicates if company is verified
    is_company_verified = ndb.BooleanProperty(default=True)
    # Flag to indicate if company is test
    is_test = ndb.BooleanProperty(default=False)
    "-----------------------------------------------------------------------------------------------------------" \
 \
    "------------------------------------------ QR-Scan Attributes --------------------------------"
    # Indicates if company has enabled sign-in via qr_code for its entities
    allow_sign_in_via_qr = ndb.BooleanProperty(default=False)
    # Settings containing relative information related to qr_code and if settings updated/qr-mode selected once or not.
    qr_settings = ndb.StructuredProperty(QrSettingsInfo)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ Enterprise Login Attributes --------------------------------"
    # Indicates if company has enforced sign-in via SSO for all its entities
    allow_enterprise_login = ndb.BooleanProperty(default=False)

    # To control okta SSO
    enable_okta_sso = ndb.BooleanProperty(default=False)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ SMS Consent Information --------------------------------"
    # Indicates if company has provided sms consent information or not
    sms_consent_provided = ndb.IntegerProperty(
        choices=[ConsentProvidedType.INACTIVE, ConsentProvidedType.NO, ConsentProvidedType.YES,
                 ConsentProvidedType.GET_EVERYTIME],
        default=ConsentProvidedType.INACTIVE)
    sms_consent_information = ndb.JsonProperty()

    "-----------------------------------------------------------------------------------------------------------"

    def get_id(self):
        return self._key.id()

    def get_urlsafe_id(self):
        return self._key.urlsafe()
