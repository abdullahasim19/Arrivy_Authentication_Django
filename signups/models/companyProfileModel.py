from django.db import models
from .userModel import ArrivyUser
from .userProfileModel import CompanyType
from signups.extraClasses import *


class OldExternalIntegration(models.Model):
    samsara_access_token = models.CharField(max_length=100)
    samsara_group_ids = models.IntegerField()


class CRMServiceInfo(models.Model):
    crm_type = models.IntegerField(
        choices=[
            (ExternalIntegrationType.PIPEDRIVE, 'Pipedrive'),
        ])
    crm_id = models.IntegerField  # deal_id of pipe_drive


class CustomIntegrationInfo(models.Model):
    integration_type = models.IntegerField()


class QrSettingsInfo(models.Model):
    mode = models.IntegerField(
        choices=[(QRSettingsModesTypes.AUTO, 'Auto'), (QRSettingsModesTypes.MANUAL, 'Manual'),
                 (QRSettingsModesTypes.MIGRATION, 'Migration'),
                 (QRSettingsModesTypes.NO_MODE, 'Mode')],
        default=QRSettingsModesTypes.AUTO)

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()
    updated_by_user = models.CharField(max_length=100)


class CompanyProfile(models.Model):
    companychoices = [
        (CompanyType.MOVING, "Moving"),
        (CompanyType.DELIVERY, 'Delivery'),
        (CompanyType.FOODDELIVERY, "Food Delivery"),
        (CompanyType.MAIDSERVICE, "Maid Service"),
        (CompanyType.HOMECARE, "Homecare"),
        (CompanyType.SERVICE, "Service"),
        (CompanyType.OTHER, "Other"),
        (CompanyType.COMMERCIALSERVICES, "Commercial Services"),
        (CompanyType.CONSTRUCTIONS, "Constructions"),
        (CompanyType.DELIVERYLOGISTICS, "Delivery Logistics"),
        (CompanyType.EVENT, "Event"),
        (CompanyType.FIELDHEALTHCARE, "Field Health Care"),
        (CompanyType.FIELDSALES, "Field Sales"),
        (CompanyType.HOMESERVICES, "Home Services"),
        (CompanyType.INSPECTIONS, "Inspections"),
        (CompanyType.INTERNETSERVICEPROVIDER, "ISP"),
        (CompanyType.SECURITY, "Security"),
        (CompanyType.SOLAR, "Solar"),
        (CompanyType.UTILITY, "Utility"),
        (CompanyType.ROOFING, "Roofing")
    ]
    owner = models.ForeignKey(ArrivyUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    exact_location = models.CharField(max_length=100, blank=True, null=True)
    # we don't need to set any default value here as we are unsure about the state of old customers and
    # we can not assume any value for them
    is_address_geo_coded = models.BooleanField(blank=True, null=True)

    country = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    support_email = models.CharField(max_length=100, blank=True, null=True)
    intro = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(null=True, blank=True)
    company_type = models.IntegerField(
        choices=companychoices,
        default=CompanyType.SERVICE)

    plan_id = models.IntegerField(default=PlanType.TEAM_MEMBERS)
    plan = models.CharField(default=convert_plan_type_to_text(PlanType.TEAM_MEMBERS), max_length=100)
    reminder_notification_time = models.IntegerField(default=0)
    reminder_notification_time_hours = models.IntegerField(default=DEFAULT_TASK_REMINDER_NOTIFICATION_TIME)
    team_reminder_queued_task_name = models.CharField(max_length=100, blank=True, null=True)
    emergency = models.CharField(max_length=100, blank=True, null=True)
    image_id = models.IntegerField()
    image_path = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    social_links = models.JSONField()
    default_entity_id = models.IntegerField()
    timezone = models.CharField(max_length=100, blank=True, null=True)
    acquisition_source = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trial_expiration_date = models.DateField(blank=True, null=True)
    discount = models.IntegerField(default=0)
    additional_charges = models.JSONField()
    time_reporting_permissions = models.JSONField()
    short_day_format = models.BooleanField(default=False)
    full_day_format = models.BooleanField(default=False)

    enable_customer_task_confirmation = models.BooleanField(default=False)
    enable_late_and_no_show_notification = models.BooleanField(default=False)
    mark_task_late_when = models.CharField(default="one_assignee_is_late", max_length=100, blank=True, null=True)
    min_acceptable_rating = models.IntegerField(default=4)
    custom_webhook = models.CharField(max_length=100, blank=True, null=True)
    custom_webhook_authentication_keys = models.JSONField()
    color = models.CharField(max_length=100, blank=True, null=True)
    pending_review_reminder_attempts = models.IntegerField(default=DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS)
    ratings_fetch_URL = models.CharField(max_length=100, blank=True, null=True)
    ratings_fetch_URL_authentication_keys = models.JSONField()
    ratings_fetch_URL_v2 = models.CharField(max_length=100, blank=True, null=True)
    ratings_fetch_URL_v2_authentication_keys = models.JSONField()
    enable_team_confirmation = models.BooleanField(default=False)
    team_confirmation_time = models.TimeField(blank=True, null=True)
    calender_start_time = models.TimeField(blank=True, null=True)
    calender_end_time = models.TimeField(blank=True, null=True)
    team_confirmation_time_zone = models.CharField(max_length=100, blank=True, null=True)
    team_confirmation_day = models.IntegerField()
    team_confirmation_notification_type = models.CharField(max_length=100, blank=True, null=True)
    team_confirmation_type = models.IntegerField(choices=[
        (TeamConfirmationType.SCHEDULE, 'Schedule'),
        (TeamConfirmationType.INSTANT, 'Instant')],
        default=TeamConfirmationType.SCHEDULE)
    team_confirmation_custom_message = models.CharField(max_length=100, blank=True, null=True)
    # change_reschedule_status_title is not using anymore
    change_reschedule_status_title = models.BooleanField(default=False)
    team_confirmation_queued_task_name = models.CharField(max_length=100, blank=True, null=True)
    rating_type = models.CharField(default=DEFAULT_RATING_TYPE, max_length=100)
    rating_threshold = models.IntegerField()
    review_response_delay = models.IntegerField(default=DEFAULT_REVIEW_RESPONSE_DELAY)
    exceptions = models.JSONField()
    samsara_integration_info = models.OneToOneField(OldExternalIntegration, on_delete=models.CASCADE)
    task_notifications_settings = models.JSONField()
    status_priority = models.JSONField()
    mileage_unit = models.IntegerField()
    calendar_week_starts_from = models.CharField(max_length=100, blank=True, null=True)
    calendar_week_ends_on = models.CharField(max_length=100, blank=True, null=True)
    is_documents_disabled = models.BooleanField(default=True)
    filters = models.JSONField()
    time_line_filters = models.JSONField()
    signup_channel = models.IntegerField(choices=[
        (InvitationChannelType.EMAIL, 'Email'),
        (InvitationChannelType.SMS, 'SMS'),
        (InvitationChannelType.USERNAME, 'Username')
    ],
        default=InvitationChannelType.EMAIL)
    signup_address = models.CharField(default=None, max_length=100)
    can_field_crew_view_contact_info = models.BooleanField(default=True)
    reminder_time_after_task_creation = models.IntegerField(default=0)
    route_start = models.IntegerField(
        choices=[(RouteStartPoint.GROUP, 'Group'),
                 (RouteStartPoint.TASK, 'Task')],
        default=RouteStartPoint.GROUP
    )
    depot_departure_time = models.TimeField()
    additional_addresses = models.JSONField()
    show_route_editing_instructions = models.BooleanField(default=True)
    auto_fill_customer_address = models.BooleanField(default=True)
    can_customer_mark_statuses = models.BooleanField(default=False)

    # Enterprise branding fields.
    show_brand_color = models.BooleanField(default=False)
    custom_message_template = models.CharField(max_length=100, blank=True, null=True)
    email_domain = models.CharField(max_length=100, blank=True, null=True)
    livetrack_base_url = models.CharField(max_length=100, blank=True, null=True)
    default_email_sender = models.CharField(max_length=100, blank=True, null=True)
    livetrack_company_name = models.CharField(max_length=100, blank=True, null=True)
    email_sender = models.CharField(max_length=100, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)

    # TODO: we need to move the above enterprise branding fields inside these JSON property
    white_labeling_settings = models.JSONField()  # This should always hold authentication keys of third party platforms like Twilio and should never be exposed publicily
    white_labeling_public_settings = models.JSONField()
    white_label_enabled = models.BooleanField(default=False)

    enforce_group_company_timezone_on_customer_communication = models.BooleanField(default=False)
    enable_inventory = models.BooleanField(default=False)
    is_on_boarding_guide_visited = models.BooleanField(default=False)
    self_scheduling = models.BooleanField(default=False)
    enable_customer_view_settings_for_scheduler = models.BooleanField(default=False)
    send_task_reminders_according_to_work_week_settings = models.BooleanField(default=True)

    crm_services_info = models.OneToOneField(CRMServiceInfo, on_delete=models.CASCADE)

    enable_safety_measures = models.BooleanField(default=False)
    safety_measures_title = models.CharField(max_length=100, blank=True, null=True)
    safety_measures = models.TextField(blank=True, null=True)
    default_time_interval = models.IntegerField(default=30)

    is_localization_enabled = models.BooleanField(default=False)
    show_time_zone_name_in_notifications = models.BooleanField(default=False)
    use_company_or_group_time_zone_for_internal_notifications = models.BooleanField(default=False)
    show_social_links_on_live_track = models.BooleanField(default=True)

    ui_filters_settings = models.JSONField()

    enable_multi_day = models.BooleanField(default=True)

    # This flag has been retired and should NEVER be used
    auto_clock_out_on_complete = models.BooleanField(default=False)

    default_locale = models.CharField(max_length=100, blank=True, null=True)
    locale_date_format = models.CharField(max_length=100, blank=True, null=True)
    locale_time_format = models.CharField(max_length=100, blank=True, null=True)
    show_directions_on_live_track = models.BooleanField(default=True)

    enable_pdf_stitching = models.BooleanField(default=False)
    enable_pdf_annotations = models.BooleanField(default=False)
    form_pdf_scale_ios = models.FloatField(default=.75)
    form_pdf_scale_web = models.FloatField(default=1.5)

    # TODO: we need the default value as True after the proper feature release
    enable_time_reporting = models.BooleanField(default=False)

    # Attributes to be used in Kiosk mode
    allow_kiosk_mode = models.BooleanField(default=False)
    username_prefix = models.CharField(max_length=100, blank=True, null=True)
    auto_logout_after = models.IntegerField()  # in seconds

    enable_sms_notifications = models.BooleanField(default=False)
    # enable_status_priority_sms_notifications is deprecated
    enable_status_priority_sms_notifications = models.BooleanField(default=False)

    can_create_booking_only = models.BooleanField(default=False)

    # kiosk_configuration = ndb.StructuredProperty(KioskConfiguration)

    # Flag to trigger Form Auto Save
    auto_save_form = models.BooleanField(default=False)

    # Flag to decide whether to apply filters on unscheduled bucket or not
    apply_filters_on_unscheduled_bucket = models.BooleanField(default=False)

    # Flag to decide whether to open task or activity form on tasks views
    choose_between_activity_or_tasks = models.BooleanField(default=False)

    # Flag to decide whether to show tasks scheduled confirmation modal
    do_not_show_tasks_scheduled_modal = models.BooleanField(default=False)

    # To control crew availability feature
    enable_crew_availability = models.BooleanField(default=False)
    allow_auto_approval_of_crew_availability_requests = models.BooleanField(default=True)
    permission_groups_that_can_approve_crew_availability_requests = models.CharField(max_length=100)

    # To control recurring tasks feature
    enable_recurring_tasks = models.BooleanField(default=False)

    # For sending task create webhook when a booking task is rescheduled.
    send_task_create_webhook_on_booking_reschedule = models.BooleanField(default=False)

    # For Sending company_support an email whenever some integration sync is failed
    send_email_on_sync_fail = models.BooleanField(default=False)
    # enable API permissions for specific companies
    is_api_enabled = models.BooleanField(default=False)
    # Used for MY PORTER to hide reviews tab.
    show_reviews_to_viewer = models.BooleanField(default=True)
    # To control high density route planning feature
    enable_high_density_route_planning = models.BooleanField(default=False)
    # To control customer template custom section
    enable_customer_templates_custom_section = models.BooleanField(default=False)
    # To enable dock scheduling feature
    enable_dock_scheduling = models.BooleanField(default=False)

    # To skip form filling step in forms
    skip_form_filling_step = models.BooleanField(default=False)

    # To control time constraints in booking calendar
    enable_travel_time_constraint_on_booking = models.BooleanField(default=False)

    # To control customer portal feature
    enable_customer_portal = models.BooleanField(default=False)
    customer_portal_domain_name = models.CharField(max_length=100, blank=True, null=True)

    # To control Elastic search feature
    enable_elastic_search = models.BooleanField(default=False)
    # To enable image compression on File uploads(i.e imageUpload Component)
    enable_image_compression = models.BooleanField(default=True)
    "--------------------------------- Custom Integrations Configurations --------------------------------------"
    custom_integrations = models.OneToOneField(CustomIntegrationInfo, on_delete=models.CASCADE)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------- Premium features control flags and billing attributes ---------------------------"
    # Any addition in the feature control flags should also be made in "get_premium_features_attribute_names" function
    enable_route_editing = models.BooleanField(default=False)
    enable_forms = models.BooleanField(default=False)
    enable_booking_schedule = models.BooleanField(default=False)
    enable_map_view = models.BooleanField(default=False)

    is_premium_enabled = models.BooleanField(default=False)

    # Example object: {"Route Editing": {"price": 250, "discount": 10}, "Forms": {"price": 100, "discount": 10}}
    premium_charges_details = models.JSONField()

    # When is plan is changed from Premium to Standard, we still need to provide premium features to the company till
    # next charge and also charge them as premium customer. This attr will hold the info that the plan of the company
    # need to be changed to Standard on the billing day.
    change_plan_to = models.CharField(max_length=100, blank=True, null=True)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ Analytics Attributes -------------------------------------------"
    # When business was contact for the first time
    contact_date = models.DateTimeField()

    # when businesses subscribe
    subscribe_date = models.DateTimeField()

    # when businesses unsubscribe
    tombstone_date = models.DateTimeField()

    # indicates businesses crm status
    crm_status = models.CharField(default="LEAD", blank=True, null=True, max_length=100)

    # indicates business crm type
    crm_business_type = models.CharField(default="INTEGRATED", max_length=100)
    # indicates the business industry
    crm_business_industry = models.CharField(default="SERVICE", max_length=100)

    # when on-boarding of a business started
    onboarding_date = models.DateTimeField()

    # indicates the number of team members for company
    company_size = models.CharField(max_length=100, blank=True, null=True)

    # indicates the list of features which are to be used by the company
    features = models.CharField(max_length=100, blank=True, null=True)

    # indicates the list of internal integrations which are used by the company
    internal_integrated_softwares = models.CharField(max_length=100, blank=True, null=True)

    # indicates the list of external integrations which are used by the company
    external_integrated_softwares = models.CharField(max_length=100, blank=True, null=True)

    # indicates the onboarding details provided by the company
    onboarding_details = models.CharField(max_length=100, blank=True, null=True)

    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ Account Verification Attributes --------------------------------"
    # Indicates if company is verified
    is_company_verified = models.BooleanField(default=True)
    # Flag to indicate if company is test
    is_test = models.BooleanField(default=False)
    "-----------------------------------------------------------------------------------------------------------" \
 \
    "------------------------------------------ QR-Scan Attributes --------------------------------"
    # Indicates if company has enabled sign-in via qr_code for its entities
    allow_sign_in_via_qr = models.BooleanField(default=False)
    # Settings containing relative information related to qr_code and if settings updated/qr-mode selected once or not.
    qr_settings = models.OneToOneField(QrSettingsInfo, on_delete=models.CASCADE)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ Enterprise Login Attributes --------------------------------"
    # Indicates if company has enforced sign-in via SSO for all its entities
    allow_enterprise_login = models.BooleanField(default=False)

    # To control okta SSO
    enable_okta_sso = models.BooleanField(default=False)
    "-----------------------------------------------------------------------------------------------------------"

    "------------------------------------------ SMS Consent Information --------------------------------"
    # Indicates if company has provided sms consent information or not
    sms_consent_provided = models.IntegerField(
        choices=[(ConsentProvidedType.INACTIVE, 'Inactive'), (ConsentProvidedType.NO, 'No'),
                 (ConsentProvidedType.YES, 'Yes'),
                 (ConsentProvidedType.GET_EVERYTIME, 'Everytime')],
        default=ConsentProvidedType.INACTIVE)
    sms_consent_information = models.JSONField()
