from django.db import models
from .userModel import ArrivyUser
from .entity import Entity
from signups.extraClasses import *
from .companyProfileModel import ExternalIntegrationType,CRMServiceInfo,OldExternalIntegration


class UserProfile(models.Model):
    companychoices=[
        (CompanyType.MOVING,"Moving"),
        (CompanyType.DELIVERY,'Delivery'),
        (CompanyType.FOODDELIVERY,"Food Delivery"),
        (CompanyType.MAIDSERVICE,"Maid Service"),
        (CompanyType.HOMECARE,"Homecare"),
        (CompanyType.SERVICE,"Service"),
        (CompanyType.OTHER,"Other"),
        (CompanyType.COMMERCIALSERVICES,"Commercial Services"),
        (CompanyType.CONSTRUCTIONS,"Constructions"),
        (CompanyType.DELIVERYLOGISTICS,"Delivery Logistics"),
        (CompanyType.EVENT,"Event"),
        (CompanyType.FIELDHEALTHCARE,"Field Health Care"),
        (CompanyType.FIELDSALES,"Field Sales"),
        (CompanyType.HOMESERVICES,"Home Services"),
        (CompanyType.INSPECTIONS,"Inspections"),
        (CompanyType.INTERNETSERVICEPROVIDER,"ISP"),
        (CompanyType.SECURITY,"Security"),
        (CompanyType.SOLAR,"Solar"),
        ( CompanyType.UTILITY,"Utility"),
        ( CompanyType.ROOFING,"Roofing")
    ]
    owner=models.ForeignKey(ArrivyUser,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    exact_location=models.CharField(max_length=100)
    is_address_geo_coded = models.BooleanField(blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    phone1 = models.CharField(max_length=100,blank=True,null=True)
    phone2 = models.CharField(max_length=100,blank=True,null=True)
    support_email = models.CharField(max_length=100,blank=True,null=True)
    intro = models.CharField(max_length=100,blank=True,null=True)
    details = models.CharField(max_length=100,blank=True,null=True)
    companytype=models.IntegerField(choices=companychoices,default=CompanyType.SERVICE)
    plan_id = models.IntegerField(default=PlanType.TEAM_MEMBERS)
    plan = models.CharField(default=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),max_length=100)
    reminder_notification_time = models.IntegerField(default=0)
    reminder_notification_time_hours = models.IntegerField(default=DEFAULT_TASK_REMINDER_NOTIFICATION_TIME)
    emergency = models.CharField(max_length=100,blank=True,null=True)
    image_id = models.IntegerField(blank=True,null=True)
    image_path = models.CharField(max_length=100,blank=True,null=True)
    website = models.CharField(max_length=100,blank=True,null=True)
    social_links = models.JSONField(blank=True,null=True)
    company_owned = models.BooleanField(blank=True,null=True)
    company_entity_id = models.ForeignKey(Entity,on_delete=models.CASCADE)# has to be foreign key from entity model
    owned_company_id = models.IntegerField(blank=True,null=True)
    default_entity_id = models.IntegerField(blank=True,null=True)#should be foreign key?
    timezone = models.CharField(max_length=100,blank=True,null=True)
    acquisition_source = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trial_expiration_date = models.DateField(blank=True,null=True)
    discount = models.IntegerField(default=0)
    additional_charges = models.JSONField(blank=True,null=True)
    self_scheduling = models.BooleanField(default=False)

    enable_customer_task_confirmation = models.BooleanField(default=False)
    enable_late_and_no_show_notification = models.BooleanField(default=False)
    min_acceptable_rating = models.IntegerField(default=4)
    custom_webhook = models.CharField(max_length=100)
    custom_webhook_authentication_keys = models.JSONField(blank=True,null=True)
    color = models.CharField(max_length=100,blank=True,null=True)
    pending_review_reminder_attempts = models.IntegerField(default=DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS)
    ratings_fetch_URL = models.CharField(max_length=100,blank=True,null=True)
    ratings_fetch_URL_authentication_keys = models.JSONField(blank=True,null=True)
    ratings_fetch_URL_v2 = models.CharField(max_length=100,blank=True,null=True)
    ratings_fetch_URL_v2_authentication_keys = models.JSONField(blank=True,null=True)
    enable_team_confirmation = models.BooleanField(default=False)
    team_confirmation_time = models.TimeField(blank=True,null=True)
    calender_start_time = models.TimeField(blank=True,null=True)
    calender_end_time = models.TimeField(blank=True,null=True)
    team_confirmation_time_zone = models.CharField(max_length=100,blank=True,null=True)
    team_confirmation_day = models.IntegerField(blank=True,null=True)
    team_confirmation_notification_type = models.CharField(max_length=100,blank=True,null=True)
    team_confirmation_custom_message = models.CharField(max_length=100,blank=True,null=True)

    team_confirmation_queued_task_name = models.CharField(max_length=100,blank=True,null=True)
    rating_type = models.CharField(default=DEFAULT_RATING_TYPE,max_length=100)
    review_response_delay = models.IntegerField(default=DEFAULT_REVIEW_RESPONSE_DELAY)

    exceptions =models.JSONField(blank=True,null=True)
    samsara_integration_info = models.OneToOneField(OldExternalIntegration,on_delete=models.CASCADE,blank=True,null=True)
    task_notifications_settings = models.JSONField(blank=True,null=True)
    status_priority =models.JSONField(blank=True,null=True)
    mileage_unit = models.IntegerField(blank=True,null=True)
    calendar_week_starts_from = models.CharField(max_length=100,blank=True,null=True)
    calendar_week_ends_on =models.CharField(max_length=100,blank=True,null=True)
    is_documents_disabled = models.BooleanField(default=True)
    filters = models.JSONField(blank=True,null=True)
    time_line_filters = models.JSONField(blank=True,null=True)
    can_field_crew_view_contact_info = models.BooleanField(default=True)
    reminder_time_after_task_creation = models.IntegerField(default=0)
    signup_channel = models.IntegerField(choices=[
        (InvitationChannelType.EMAIL,'Email'),
         (InvitationChannelType.SMS,'SMS'),
          (InvitationChannelType.USERNAME,'username')
    ], default=InvitationChannelType.EMAIL)
    signup_address = models.CharField(default=None,max_length=100)
    route_start = models.IntegerField(
        choices=[(RouteStartPoint.GROUP,'Group'),
                 (RouteStartPoint.TASK,'Task')],
        default=RouteStartPoint.GROUP
    )
    enable_route_editing = models.BooleanField(default=False)
    additional_addresses = models.JSONField(blank=True,null=True)
    show_route_editing_instructions = models.BooleanField(blank=True,null=True)
    auto_fill_customer_address = models.BooleanField(default=True)

    # Enterprise branding fields.
    show_brand_color = models.BooleanField(default=False)
    custom_message_template = models.CharField(max_length=100,blank=True,null=True)
    email_domain = models.CharField(max_length=100,blank=True,null=True)
    livetrack_base_url = models.CharField(max_length=100,blank=True,null=True)
    default_email_sender = models.CharField(max_length=100,blank=True,null=True)
    white_label_enabled = models.BooleanField(default=False)
    livetrack_company_name = models.CharField(max_length=100)

    enforce_group_company_timezone_on_customer_communication = models.BooleanField(default=False)
    enable_inventory = models.BooleanField(default=False)
    is_on_boarding_guide_visited = models.BooleanField(default=False)
    enable_customer_view_settings_for_scheduler = models.BooleanField(default=False)
    send_task_reminders_according_to_work_week_settings = models.BooleanField(default=True)

    enable_forms = models.BooleanField(default=False)
    crm_services_info = models.OneToOneField(CRMServiceInfo,on_delete=models.CASCADE,blank=True,null=True)

    enable_safety_measures = models.BooleanField(default=False)
    safety_measures_title = models.CharField(max_length=100,blank=True,null=True)
    safety_measures = models.CharField(max_length=100,blank=True,null=True)
    default_time_interval = models.IntegerField(default=30)

    is_premium_enabled = models.BooleanField(default=False)
    # Example object: {"Route Editing": {"price": 250, "discount": 10}, "Forms": {"price": 100, "discount": 10}}
    premium_charges_details = models.JSONField(blank=True,null=True)

    is_localization_enabled = models.BooleanField(default=False)

    