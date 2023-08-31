class EntityInviteStatus:
    def __init__(self):
        pass

    PENDING = 7001
    ACCEPTED = 7002


class EntityUserTypes:
    def __init__(self):
        pass

    CUSTOMER = 1000
    CREW = 1002

    @classmethod
    def get_all_entity_user_types(cls):
        return [cls.CUSTOMER, cls.CREW]


class InvitationChannelType:
    EMAIL = 3001
    SMS = 3002
    USERNAME = 30003

    @classmethod
    def get_all_invitation_channel_types(cls):
        return [cls.EMAIL, cls.SMS, cls.USERNAME]


class CompanyType:
    MOVING = 1001
    FOODDELIVERY = 1002
    MAIDSERVICE = 1003
    OTHER = 1004
    DELIVERY = 1005
    HOMECARE = 1006
    SERVICE = 1007
    COMMERCIALSERVICES = 1008
    CONSTRUCTIONS = 1009
    DELIVERYLOGISTICS = 1010
    EVENT = 1011
    FIELDHEALTHCARE = 1012
    FIELDSALES = 1013
    HOMESERVICES = 1014
    INSPECTIONS = 1015
    INTERNETSERVICEPROVIDER = 1016
    SECURITY = 1017
    SOLAR = 1018
    UTILITY = 1019
    ROOFING = 1020


class PlanType:
    TEAM_MEMBERS = 1
    ENTERPRISE = 2


def convert_plan_type_to_text(type):
    if type == PlanType.TEAM_MEMBERS:
        return 'TEAM MEMBERS'
    elif type == PlanType.ENTERPRISE:
        return 'ENTERPRISE'
    else:
        return 'TEAM MEMBERS'


def convert_plan_text_to_plan_type(text):
    if text == 'TEAM MEMBERS':
        return PlanType.TEAM_MEMBERS
    elif text == 'ENTERPRISE':
        return PlanType.ENTERPRISE
    else:
        return PlanType.TEAM_MEMBERS


DEFAULT_TASK_REMINDER_NOTIFICATION_TIME = -1
DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS = 2
DEFAULT_RATING_TYPE = 'FiveStar'
DEFAULT_REVIEW_RESPONSE_DELAY = -1


class TeamConfirmationType:
    SCHEDULE = 1000
    INSTANT = 1001


class RouteStartPoint:
    GROUP = 1001
    TASK = 1002


class ConsentProvidedType:
    INACTIVE = 1000  # Inactive means we do not have any information regarding consent yet
    NO = 1001  # No means customer have not provided consent, so not sms will be sent
    YES = 1002  # Yes means customer have provided consent evidence information
    GET_EVERYTIME = 1003  # Get_everytime means we will send opt-in message to customer for every task before sending original message

    @classmethod
    def get_all_consnet_provided_options_types(cls):
        return [ConsentProvidedType.INACTIVE, ConsentProvidedType.NO, ConsentProvidedType.YES,
                ConsentProvidedType.GET_EVERYTIME]


class ExternalIntegrationType:
    SAMSARA = 4000
    MOVERBASE = 4001
    CURRENT_RMS = 4002
    VONIGO = 4003
    MOVERS_SUITE = 4004
    PIPEDRIVE = 4005
    CALENDLY = 4006
    HUBSPOT = 4007
    ZOHO = 4008
    SHOPIFY = 4009
    SALESFORCE = 4010
    INFUSIONSOFT = 4012
    MOVERS_SUITE_VENDOR_CONNECT = 4013
    WORKDAY = 4014
    SHAG_CARPET = 4016
    ACTIVECAMPAIGN = 4015
    SQUARE = 4017
    GOOGLEDRIVE = 4018
    MOVERS_SUITE_ATTACHMENT = 4019
    COMPANYCAM = 4020
    QUICKBASE = 4021
    INTERCOM = 4022
    ZOHO_BOOKS = 4023
    QUICKBOOKS = 4024
    ZOHO_INVENTORY = 4025
    FOLLOWUPBOSS = 4026
    COPPER = 4027
    EGNYTE = 4028
    XERO = 4029
    ONEDRIVE = 4030
    MICROSOFT_DYNAMICS = 4031
    XERO_PAYROLL = 4032
    GOOGLECALENDAR = 4033
    HUBSPOT_ATTACHMENT = 4034
    MICROSOFT_DYNAMICS_SALES = 4035

    @classmethod
    def get_all_integration_types(cls):
        return [cls.SAMSARA, cls.MOVERBASE, cls.CURRENT_RMS, cls.VONIGO, cls.MOVERS_SUITE, cls.PIPEDRIVE, cls.CALENDLY,
                cls.HUBSPOT, cls.ZOHO, cls.SALESFORCE, cls.INFUSIONSOFT, cls.MOVERS_SUITE_VENDOR_CONNECT, cls.WORKDAY,
                cls.SHAG_CARPET, cls.ACTIVECAMPAIGN, cls.SQUARE, cls.GOOGLEDRIVE, cls.MOVERS_SUITE_ATTACHMENT,
                cls.COMPANYCAM, cls.SHOPIFY, cls.QUICKBASE, cls.INTERCOM, cls.ZOHO_BOOKS, cls.QUICKBOOKS,
                cls.ZOHO_INVENTORY, cls.FOLLOWUPBOSS, cls.COPPER, cls.EGNYTE, cls.XERO, cls.GOOGLECALENDAR,
                cls.ONEDRIVE,
                cls.MICROSOFT_DYNAMICS, cls.XERO_PAYROLL, cls.HUBSPOT_ATTACHMENT, cls.MICROSOFT_DYNAMICS_SALES]

    @classmethod
    def get_all_custom_integration_types(cls):
        return [cls.SHAG_CARPET]

    @classmethod
    def get_all_payment_integration_types(cls):
        return [cls.SQUARE, cls.QUICKBOOKS, cls.XERO]

    @classmethod
    def get_all_non_data_fetch_module_integration_types(cls):
        return [cls.PIPEDRIVE, cls.ZOHO, cls.HUBSPOT, cls.SALESFORCE, cls.SHOPIFY]

    @classmethod
    def get_all_integration_types_that_support_forms(cls):
        return [cls.MOVERS_SUITE]

    @classmethod
    def get_all_integration_types_that_support_payment_invoice(cls):
        return [cls.SQUARE, cls.QUICKBOOKS, cls.XERO]


class QRSettingsModesTypes:
    AUTO = 1001
    MANUAL = 1002
    MIGRATION = 1003
    NO_MODE = 1004

    @classmethod
    def get_all_qr_settings_modes_types(cls):
        return [QRSettingsModesTypes.AUTO, QRSettingsModesTypes.MANUAL, QRSettingsModesTypes.MIGRATION,
                QRSettingsModesTypes.NO_MODE]


class TaskStatusType:
    """
    MAKE SURE THIS TYPE DO NOT OVERLAP WITH NotificationTriggerType
    """

    NOTSTARTED = 1001
    ENROUTE = 1002
    STARTED = 1003
    COMPLETE = 1004
    CANCELLED = 1005
    EXCEPTION = 1006
    CUSTOM = 1007
    PREPARING = 1008
    READYFORPICKUP = 1009
    CONFIRMED = 1010
    RESCHEDULED = 1011

    ARRIVING = 1050
    LATE = 1051
    NOSHOW = 1052
    EXTRA_TIME = 1053
    PREDICTED_LATE = 1054

    REMINDER = 1100
    RECOMMENDED = 1102
    REVIEW_REMINDER = 1103
    CUSTOMER_SIGNATURE = 1104
    CUSTOMER_EXCEPTION = 1105
    SEEN_BY_CUSTOMER = 1106
    CREW_ASSIGNED = 1107
    CREW_REMOVED = 1108
    EQUIPMENT_ASSIGNED = 1109
    EQUIPMENT_REMOVED = 1110
    BOOKING_CANCELLED = 1111

    ON_HOLD = 1201
    MOVING_TO_STORAGE = 1202
    IN_STORAGE = 1203
    OUT_OF_STORAGE = 1204
    IN_TRANSIT = 1205
    PICKING_UP = 1206
    MILESTONE = 1207
    CLOSED = 1208

    ARRIVED = 1301
    DEPARTED = 1302
    AUTO_START_PENDING = 1303
    AUTO_START = 1304
    AUTO_COMPLETE_PENDING = 1305
    AUTO_COMPLETE = 1306
    RETURNED = 1307

    ORDER = 1401
    SKIP = 1402

    SUBSCRIBED = 1501
    UNSUBSCRIBED = 1502
    HELP = 1503

    LAUNCH_DOCUMENT = 1504
    MANUAL_NOTIFICATION = 1505
    FILE_ANNOTATED = 1506

    CHECKINVENTORY = 1601
    CHECKSUPPLIES = 1602

    RESEND_TASK_CONFIRMATION = 1701

    TASK_ACCEPTED = 1801
    TASK_REJECTED = 1802

    FORM_COMPLETE = 1901
    FORM_SUBMIT = 1902
    FORM_ATTACH = 1903
    FORM_REMINDER = 1904

    DAY_START = 2000
    DAY_COMPLETE = 2002

    CLOCK_IN = 2101
    CLOCK_OUT = 2102

    PROCESS_PAYMENT = 2200

    INVOICE_GENERATED = 2300
    PAYMENT_MADE = 2301

    INTEGRATION = 2400

    OPT_IN_MESSAGE_SENT = 2500
    CONSENT_PENDING = 2501

    @classmethod
    def get_all_task_status_types(cls):
        return [TaskStatusType.NOTSTARTED, TaskStatusType.ENROUTE, TaskStatusType.STARTED, TaskStatusType.COMPLETE,
                TaskStatusType.CANCELLED, TaskStatusType.EXCEPTION, TaskStatusType.CUSTOM, TaskStatusType.PREPARING,
                TaskStatusType.READYFORPICKUP, TaskStatusType.CONFIRMED, TaskStatusType.RESCHEDULED,
                TaskStatusType.BOOKING_CANCELLED, TaskStatusType.ARRIVING, TaskStatusType.LATE,
                TaskStatusType.PREDICTED_LATE, TaskStatusType.NOSHOW,
                TaskStatusType.EXTRA_TIME, TaskStatusType.REMINDER, TaskStatusType.RECOMMENDED,
                TaskStatusType.REVIEW_REMINDER, TaskStatusType.CUSTOMER_SIGNATURE, TaskStatusType.CUSTOMER_EXCEPTION,
                TaskStatusType.SEEN_BY_CUSTOMER, TaskStatusType.CREW_ASSIGNED, TaskStatusType.CREW_REMOVED,
                TaskStatusType.EQUIPMENT_ASSIGNED, TaskStatusType.EQUIPMENT_REMOVED, TaskStatusType.ON_HOLD,
                TaskStatusType.MOVING_TO_STORAGE, TaskStatusType.IN_STORAGE, TaskStatusType.OUT_OF_STORAGE,
                TaskStatusType.IN_TRANSIT, TaskStatusType.PICKING_UP, TaskStatusType.ARRIVED, TaskStatusType.DEPARTED,
                TaskStatusType.AUTO_START_PENDING, TaskStatusType.AUTO_START, TaskStatusType.AUTO_COMPLETE_PENDING,
                TaskStatusType.AUTO_COMPLETE, TaskStatusType.RETURNED, TaskStatusType.ORDER, TaskStatusType.SKIP,
                TaskStatusType.SUBSCRIBED, TaskStatusType.UNSUBSCRIBED, TaskStatusType.HELP,
                TaskStatusType.LAUNCH_DOCUMENT, TaskStatusType.MANUAL_NOTIFICATION, TaskStatusType.CHECKINVENTORY,
                TaskStatusType.CHECKSUPPLIES, TaskStatusType.RESEND_TASK_CONFIRMATION, TaskStatusType.TASK_ACCEPTED,
                TaskStatusType.TASK_REJECTED, TaskStatusType.FORM_COMPLETE, TaskStatusType.FORM_SUBMIT,
                TaskStatusType.FORM_ATTACH, TaskStatusType.DAY_START, TaskStatusType.DAY_COMPLETE,
                TaskStatusType.CLOCK_IN, TaskStatusType.CLOCK_OUT, TaskStatusType.PROCESS_PAYMENT,
                TaskStatusType.MILESTONE, TaskStatusType.FORM_REMINDER, TaskStatusType.INVOICE_GENERATED,
                TaskStatusType.PAYMENT_MADE, TaskStatusType.CLOSED, TaskStatusType.INTEGRATION,
                TaskStatusType.FILE_ANNOTATED, TaskStatusType.OPT_IN_MESSAGE_SENT, TaskStatusType.CONSENT_PENDING]


class DefaultStatusPriorityNames:
    def __init__(self):
        pass

    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    URGENT = 'URGENT'


class IncludeInTaskSummaryAs:
    No = 1000
    task_time = 1001
    travel_time = 1002


class NotificationTriggerType:
    # MAKE SURE THIS TYPE DO NOT OVERLAP WITH TaskStatusType
    TASK_DELETED = 1803
    TEAM_NOTE = 2001


def get_status_priorities():
    # "priority" and "same_day" are just here for reference that hold the name of the priority
    # and they should not be used anywhere. We are just keeping them for backward compatibility
    status_priorities = {
        str(TaskStatusType.NOTSTARTED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.ENROUTE): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.travel_time
        },
        str(TaskStatusType.STARTED): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.task_time
        },
        str(TaskStatusType.COMPLETE): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.task_time
        },
        str(TaskStatusType.CANCELLED): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.EXCEPTION): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CUSTOM): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.PREPARING): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.READYFORPICKUP): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CONFIRMED): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.RESCHEDULED): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.ARRIVING): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.LATE): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.PREDICTED_LATE): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.NOSHOW): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.EXTRA_TIME): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.REMINDER): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.RECOMMENDED): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.REVIEW_REMINDER): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CUSTOMER_SIGNATURE): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CUSTOMER_EXCEPTION): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.BOOKING_CANCELLED): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.SEEN_BY_CUSTOMER): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CREW_ASSIGNED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CREW_REMOVED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.EQUIPMENT_ASSIGNED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.EQUIPMENT_REMOVED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.ON_HOLD): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.MOVING_TO_STORAGE): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.IN_STORAGE): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.OUT_OF_STORAGE): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.IN_TRANSIT): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.PICKING_UP): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.ARRIVED): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.DEPARTED): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.AUTO_START_PENDING): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.AUTO_START): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.task_time
        },
        str(TaskStatusType.AUTO_COMPLETE_PENDING): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.AUTO_COMPLETE): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.task_time
        },
        str(TaskStatusType.RETURNED): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.ORDER): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.SKIP): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.SUBSCRIBED): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.UNSUBSCRIBED): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.HELP): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(NotificationTriggerType.TEAM_NOTE): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.MANUAL_NOTIFICATION): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CHECKINVENTORY): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CHECKSUPPLIES): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.RESEND_TASK_CONFIRMATION): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.FORM_COMPLETE): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.FORM_ATTACH): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.FORM_SUBMIT): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.TASK_ACCEPTED): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(NotificationTriggerType.TASK_DELETED): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.TASK_REJECTED): {
            'priority': DefaultStatusPriorityNames.URGENT,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.URGENT,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.DAY_START): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.task_time
        },
        str(TaskStatusType.DAY_COMPLETE): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            # This is a special case where we want to add this status in elapsed time calculations
            # but not in task summary
            'time_mileage': True,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CLOCK_IN): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CLOCK_OUT): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.PROCESS_PAYMENT): {
            'priority': DefaultStatusPriorityNames.HIGH,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.HIGH,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.MILESTONE): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.FORM_REMINDER): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.INVOICE_GENERATED): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.PAYMENT_MADE): {
            'priority': DefaultStatusPriorityNames.MEDIUM,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.MEDIUM,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CLOSED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.INTEGRATION): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        }, str(TaskStatusType.FILE_ANNOTATED): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.OPT_IN_MESSAGE_SENT): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        },
        str(TaskStatusType.CONSENT_PENDING): {
            'priority': DefaultStatusPriorityNames.LOW,
            'priority_id': '',
            'same_day': DefaultStatusPriorityNames.LOW,
            'same_day_priority_id': '',
            'time_mileage': False,
            'include_in_task_summary_as': IncludeInTaskSummaryAs.No
        }
    }
    return status_priorities


PERMISSION_GROUPS_THAT_CAN_APPROVE_CREW_AVAILABILITY_REQUESTS = ['Admin', 'Scheduler', 'Viewer']


class EntityUserTypeNames:
    def __init__(self):
        pass

    CUSTOMER = 'CUSTOMER'
    CREW = 'CREW'

    @classmethod
    def get_all_entity_user_names(cls):
        return [cls.CUSTOMER, cls.CREW]


def convert_entity_user_name_to_type(entity_name):
    if entity_name.upper() == EntityUserTypeNames.CUSTOMER:
        return EntityUserTypes.CUSTOMER
    elif entity_name.upper() == EntityUserTypeNames.CREW:
        return EntityUserTypes.CREW
    else:
        return EntityUserTypes.CREW


def convert_entity_user_type_to_name(entity_type):
    if entity_type == EntityUserTypes.CUSTOMER:
        return EntityUserTypeNames.CUSTOMER
    elif entity_type == EntityUserTypes.CREW:
        return EntityUserTypeNames.CREW
    else:
        return EntityUserTypeNames.CREW



class ExternalModuleType:
    def __init__(self):
        pass

    ROUTE_OPTIMIZER = 1000

    @classmethod
    def get_all_external_module_types(cls):
        return [(cls.ROUTE_OPTIMIZER,'Optimizer')]




class ActivityType:
    NOTE = 2001
    CALL = 2002
    APPOINTMENT = 2003
    TO_DO = 2004
    BREAK = 2005
    EMAIL = 2006

    @classmethod
    def get_all_activity_type(cls):
        return [cls.NOTE, cls.CALL, cls.APPOINTMENT, cls.TO_DO, cls.BREAK, cls.EMAIL]


class ShareTypes:

    INTERNAL = 1000
    PDF_ONLY = 1001
    FULL = 1002

    @classmethod
    def get_share_types(cls):
        return [cls.INTERNAL, cls.PDF_ONLY, cls.FULL]


class FormBelongsToTypes:
    TASK = 1000
    CHECKLIST_ITEM = 1001

    @classmethod
    def get_form_belongs_to_types(cls):
        return [cls.TASK, cls.CHECKLIST_ITEM]


class TaskConfirmationFinalStatus:
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    PARTIALLY_ACCEPTED = 'PARTIALLY_ACCEPTED'
    UN_RESPONDED = 'UN_RESPONDED'



class CustomerTypes:
    CUSTOMER = 5001
    LEAD = 5002


class UseDropdownLabelsAndValuesAs:
    USE_AS_LABELS = 'USE_AS_LABELS'
    USE_AS_NUMERIC = 'USE_AS_NUMERIC'
