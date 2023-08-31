from django.db import models
from signups.extraClasses import *
from signups.models.userModel import ArrivyUser


class ExtraField(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)

    # we will use this variable for multi select dropdown only
    values = models.JSONField(blank=True,null=True)

    dropdown_labels_and_values = models.JSONField(blank=True,null=True)
    use_dropdown_labels_and_values_as = models.CharField(choices=[
        (UseDropdownLabelsAndValuesAs.USE_AS_LABELS,'Labels'),
        (UseDropdownLabelsAndValuesAs.USE_AS_NUMERIC,'Numeric',)
    ],max_length=100)
    dropdown_labels_and_values_order = models.JSONField(blank=True,null=True)


class TaskEntityConfirmationStatus(models.Model):
    entity_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class FormMetaData(models.Model):
    # ID of master form
    master_form_id = models.IntegerField(blank=True, null=True)
    # ID of form submission associated with master form
    form_submission_id = models.IntegerField(blank=True, null=True)
    #share_as = models.IntegerField(choices=ShareTypes.get_share_types(), default=ShareTypes.INTERNAL)
    belongs_to = models.IntegerField(
        #choices=FormBelongsToTypes.get_form_belongs_to_types(),
        default=FormBelongsToTypes.TASK
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    # random generated hash
    hash = models.CharField(max_length=100, blank=True, null=True)
    sync_to_google_drive = models.BooleanField(default=True)
    sync_to_egnyte = models.BooleanField(default=True)
    sync_to_onedrive = models.BooleanField(default=True)


class CheckListInfo(models.Model):
    master_checklist_id = models.IntegerField(blank=True, null=True)
    task_checklist_id = models.IntegerField(blank=True, null=True)
    is_dirty = models.BooleanField(default=False)


class CheckListItemInfo(models.Model):
    master_checklist_id = models.IntegerField(blank=True, null=True)
    task_checklist_id = models.IntegerField(blank=True, null=True)
    master_checklist_item_id = models.IntegerField(blank=True, null=True)
    task_checklist_item_id = models.IntegerField(blank=True, null=True)
    is_dirty = models.BooleanField(default=False)


class AdditionalContact(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    company_name = models.CharField(max_length=100, blank=True, null=True)

    notifications = models.JSONField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField(default=False)


class ExternalModuleInfo(models.Model):
    # TO be used with Task, TaskRoute (and any other entity) to indicate its association with any external module

    #module_type = models.IntegerField(choices=ExternalModuleType.get_all_external_module_types(), blank=True, null=True)
    module_id = models.CharField(max_length=100, blank=True, null=True)
    additional_info = models.JSONField(blank=True, null=True)


class ExternalIntegrationInfo(models.Model):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    external_type = models.CharField(max_length=100, blank=True, null=True)
    external_url = models.CharField(max_length=100, blank=True, null=True)
    external_resource_type = models.CharField(max_length=100, blank=True, null=True)
    linked_external_ref = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.BooleanField(blank=True, null=True)
    update_info = models.DateTimeField(blank=True, null=True)
    delete_info = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


class Task(models.Model):
    owner = models.ForeignKey(ArrivyUser, on_delete=models.CASCADE,related_name='owner')
    created_by = models.ForeignKey(ArrivyUser, on_delete=models.CASCADE,related_name='created_by')
    updated_by = models.ForeignKey(ArrivyUser, on_delete=models.CASCADE, blank=True, null=True,related_name='updated_by')
    # created_by_user = models.CharField(max_length=100,blank=True,null=True)
    # updated_by_user = models.CharField(max_length=100,blank=True,null=True)

    source = models.CharField(max_length=100, blank=True, null=True)
    source_id = models.CharField(max_length=100, blank=True, null=True)

    template = models.IntegerField(blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)

    title = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    start_datetime_original_iso_str = models.CharField(max_length=100, blank=True, null=True)
    start_datetime_timezone = models.CharField(max_length=100, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime_original_iso_str = models.CharField(max_length=100, blank=True, null=True)
    end_datetime_timezone = models.CharField(max_length=100, blank=True, null=True)
    due_datetime = models.DateTimeField(blank=True, null=True)
    due_datetime_original_iso_str = models.CharField(max_length=100, blank=True, null=True)
    self_scheduling = models.BooleanField(default=False)
    is_without_datetime = models.BooleanField(default=False)
    # For multi-day tasks with basic schedule, this property will hold start_datetime of every day
    # and end_datetime of task as well
    basic_schedule = models.DateTimeField(blank=True, null=True)
    # If task is multi day or not
    is_multi_day = models.BooleanField(default=False)

    status = models.IntegerField(
        choices=[
            (TaskStatusType.NOTSTARTED,'Not started'),
            (TaskStatusType.ENROUTE,'Enroute'),
            (TaskStatusType.STARTED,'Started'),
            (TaskStatusType.COMPLETE,'Complete'),
            (TaskStatusType.CANCELLED,'Cancel')
        ],
        default=TaskStatusType.NOTSTARTED)

    status_id = models.IntegerField(blank=True, null=True)
    status_title = models.CharField(max_length=100, blank=True, null=True)

    notifications = models.JSONField(blank=True, null=True)
    notifications_sent = models.JSONField(blank=True, null=True)
    extra_fields = models.JSONField(blank=True, null=True)
    template_extra_fields = models.OneToOneField(ExtraField,on_delete=models.CASCADE,blank=True,null=True)
    entity_ids = models.IntegerField(blank=True, null=True)
    skill_ids = models.IntegerField(blank=True, null=True)
    document_ids = models.IntegerField(blank=True, null=True)
    resource_ids = models.IntegerField(blank=True, null=True)
    customer_first_name = models.CharField(max_length=100, blank=True, null=True)
    customer_last_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_company_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    customer_address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=100, blank=True, null=True)  # complete customer address
    customer_city = models.CharField(max_length=100, blank=True, null=True)
    customer_state = models.CharField(max_length=100, blank=True, null=True)
    customer_country = models.CharField(max_length=100, blank=True, null=True)
    customer_zipcode = models.CharField(max_length=100, blank=True, null=True)
    customer_exact_location = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    customer_mobile_number = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    customer_notes = models.CharField(max_length=100, blank=True, null=True)
    customer_timezone = models.CharField(max_length=100, blank=True, null=True)
    customer_type = models.IntegerField(choices=[
        (CustomerTypes.CUSTOMER,'Customer'),
        (CustomerTypes.LEAD,'LEAD')
    ], default=CustomerTypes.CUSTOMER)
    # we don't need to set any default value here as we are unsure about the state of old tasks and
    # we can not assume any value for them
    is_customer_address_geo_coded = models.BooleanField(blank=True, null=True)
    use_lat_lng_address = models.BooleanField(default=False)
    enable_time_window_display = models.BooleanField(blank=True, null=True)
    time_window_start = models.IntegerField(blank=True, null=True)  # in mins
    use_assignee_color = models.BooleanField(blank=True, null=True)
    # series = ndb.KeyProperty(kind='TaskSeries')
    file_ids = models.IntegerField(blank=True, null=True)
    unscheduled = models.BooleanField(default=False)
    pending_review_reminder_time = models.DateTimeField(blank=True, null=True)
    pending_review_reminder_attempts_left = models.IntegerField(blank=True, null=True)
    queued_task_name = models.CharField(max_length=100, blank=True, null=True)
    is_archived = models.BooleanField(default=False)
    is_linked = models.BooleanField(default=False)
    linked_internal_ref = models.IntegerField(blank=True, null=True)
    linked_external_ref = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    routes = models.CharField(max_length=100, blank=True, null=True)
    mileage = models.FloatField(blank=True, null=True)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    parent_task_external_id = models.CharField(max_length=100, blank=True,
                                               null=True)  # For task, with external id, duplicated through UI
    external_url = models.CharField(max_length=100, blank=True, null=True)

    additional_addresses = models.JSONField(blank=True, null=True)
    current_destination = models.JSONField(blank=True, null=True)
    # in mins
    travel_time = models.IntegerField(blank=True, null=True)
    task_time = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)

    do_not_send_webhook_notification = models.BooleanField(default=False)
    entity_confirmation_statuses = models.JSONField(blank=True, null=True)

    group_id = models.IntegerField(blank=True, null=True)

    items = models.JSONField(blank=True, null=True)

    route_id = models.CharField(max_length=100, blank=True, null=True)
    internal_route_id = models.IntegerField(blank=True, null=True)

    duration = models.IntegerField(blank=True, null=True)

    # This property is used to store team notifications in structured form.
    structured_entity_confirmation_statuses = models.OneToOneField(TaskEntityConfirmationStatus,
                                                                   on_delete=models.CASCADE, blank=True, null=True)
    # This property tells what is the team status on task. This is calculated using entity_confirmation_statuses.
    task_final_confirmation_status = models.CharField(default=TaskConfirmationFinalStatus.UN_RESPONDED, max_length=100)

    # to accommodate worker scheduling requests
    number_of_workers_required = models.IntegerField(blank=True, null=True)
    # to store reference of worker's which were assigned through worker request.
    # This will help us in the case when we want to revert assigned workers, when associated worker request is cancelled
    worker_ids = models.IntegerField(blank=True, null=True)

    # For template_type activity type is required to specify the type of activity
    activity_type = models.IntegerField(
        choices=[
            (ActivityType.NOTE,'Note'),
            (ActivityType.CALL,'Call'),
            (ActivityType.APPOINTMENT,'Appointment'),
            (ActivityType.TO_DO,'Todo'),
            (ActivityType.BREAK,'Break'),
            (ActivityType.EMAIL,'Email')
        ],
        default=ActivityType.NOTE
    )
    # for all day activity
    all_day = models.BooleanField(default=False)

    # to store source of external platform sources from which tasks are fetched using data fetch module
    external_type = models.CharField(max_length=100, blank=True, null=True)

    # for task supply
    is_supply_provided_locked = models.BooleanField(default=False)
    is_supply_returned_locked = models.BooleanField(default=False)

    forms = models.OneToOneField(FormMetaData, on_delete=models.CASCADE, blank=True, null=True)
    # Used by our UI (Routes dashboard) to maintain position of task within route
    position_in_route = models.IntegerField(blank=True, null=True)

    # Used by our UI for unscheduled task time if time fields are not given with start and end date
    task_without_time = models.BooleanField(default=False)

    # To indicate if task is locked or not
    is_locked = models.BooleanField(default=False)

    # To indicate if activity was made as a result of route publish
    is_route_activity = models.BooleanField(default=False)

    # info of the jobs booked via self scheduling booking calendar
    is_booking = models.BooleanField(default=False)
    # booking calendar id
    booking_id = models.IntegerField(blank=True, null=True)
    # booking calendar slot id
    booking_slot_id = models.IntegerField(blank=True, null=True)

    additional_info = models.JSONField(blank=True, null=True)

    external_resource_type = models.CharField(max_length=100, blank=True, null=True)
    external_live_track_link = models.TextField(blank=True, null=True)

    checklists = models.OneToOneField(CheckListInfo, on_delete=models.CASCADE,blank=True,null=True)

    checklist_items = models.OneToOneField(CheckListItemInfo, on_delete=models.CASCADE,blank=True,null=True)

    # for applying expected date ranges on unscheduled tasks
    enable_expected_date_range = models.BooleanField(default=False)
    expected_start_datetime = models.DateTimeField(blank=True, null=True)
    expected_start_datetime_original_iso_str = models.CharField(max_length=100, blank=True, null=True)
    expected_end_datetime = models.DateTimeField(blank=True, null=True)
    expected_end_datetime_original_iso_str = models.CharField(max_length=100, blank=True, null=True)

    external_integration_info = models.OneToOneField(ExternalIntegrationInfo, on_delete=models.CASCADE,blank=True,null=True)

    additional_contacts = models.OneToOneField(AdditionalContact, on_delete=models.CASCADE,blank=True,null=True)

    recurring_tasks_settings_id = models.IntegerField(blank=True, null=True)
    recurring_tasks_settings_title = models.CharField(max_length=100, blank=True, null=True)

    # Indicates the association of task with external modules
    external_module_info = models.OneToOneField(ExternalModuleInfo, on_delete=models.CASCADE,blank=True,null=True)

    # Specifically to be used when tasks are created/updated via ROUTE PUBLISHER
    # and customer communication needs to be controlled
    send_customer_communications = models.BooleanField(default=False)

    # Indicates if a task belongs to unplanned route or not. This is to be used when HDRP is enabled as in that case
    # we don't create an unplanned route and tasks belonging to unplanned route are indicated by this flag
    belongs_to_unplanned_route = models.BooleanField(default=False)
    # skills search operator for Team Explorer getEntities() call
    skills_search_operator = models.CharField(max_length=100, blank=True, null=True)

    sms_consent_meta = models.JSONField(blank=True, null=True)

    annotation_history = models.JSONField(blank=True, null=True)

    # Need to add this field in elastic search and big query in future
    slot_fields = models.JSONField(blank=True, null=True)
