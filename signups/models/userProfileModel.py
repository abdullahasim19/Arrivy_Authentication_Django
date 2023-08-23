from django.db import models
from .userModel import ArrivyUser
from .entity import Entity
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


class OldExternalIntegration(models.Model):
    samsara_access_token = models.CharField(max_length=100)
    samsara_group_ids = models.IntegerField()

class ExternalIntegrationName:
    SAMSARA = 'SAMSARA'
    MOVERBASE = 'MOVERBASE'
    CURRENT_RMS = 'CURRENT_RMS'
    VONIGO = 'VONIGO'
    MOVERS_SUITE = 'MOVERS_SUITE'
    PIPEDRIVE = 'PIPEDRIVE'
    CALENDLY = 'CALENDLY'
    HUBSPOT = 'HUBSPOT'
    ZOHO = 'ZOHO'
    SHOPIFY = 'SHOPIFY'
    SALESFORCE = 'SALESFORCE'
    INFUSIONSOFT = 'INFUSIONSOFT'
    MOVERS_SUITE_VENDOR_CONNECT = 'MOVERS_SUITE_VENDOR_CONNECT'
    WORKDAY = 'WORKDAY'
    SHAG_CARPET = 'SHAG_CARPET'
    ACTIVECAMPAIGN = 'ACTIVECAMPAIGN'
    SQUARE = 'SQUARE'
    GOOGLEDRIVE = 'GOOGLEDRIVE'
    GOOGLECALENDAR = 'GOOGLECALENDAR'
    MOVERS_SUITE_ATTACHMENT = 'MOVERS_SUITE_ATTACHMENT'
    COMPANYCAM = 'COMPANYCAM'
    QUICKBASE = 'QUICKBASE'
    INTERCOM = 'INTERCOM'
    ZOHO_BOOKS = 'ZOHO_BOOKS'
    QUICKBOOKS = 'QUICKBOOKS'
    ZOHO_INVENTORY = 'ZOHO_INVENTORY'
    FOLLOWUPBOSS = 'FOLLOWUPBOSS'
    COPPER = 'COPPER'
    EGNYTE = 'EGNYTE'
    XERO = 'XERO'
    ONEDRIVE = 'ONEDRIVE'
    MICROSOFT_DYNAMICS = 'MICROSOFT_DYNAMICS'
    XERO_PAYROLL = 'XERO_PAYROLL'
    HUBSPOT_ATTACHMENT = 'HUBSPOT_ATTACHMENT'
    MICROSOFT_DYNAMICS_SALES = 'MICROSOFT_DYNAMICS_SALES'

    @classmethod
    def get_all_integration_names(cls):
        return [cls.SAMSARA, cls.MOVERBASE, cls.CURRENT_RMS, cls.VONIGO, cls.MOVERS_SUITE, cls.PIPEDRIVE, cls.CALENDLY,
                cls.HUBSPOT, cls.ZOHO, cls.SALESFORCE, cls.INFUSIONSOFT, cls.MOVERS_SUITE_VENDOR_CONNECT, cls.WORKDAY,
                cls.SHAG_CARPET, cls.ACTIVECAMPAIGN, cls.SQUARE, cls.GOOGLEDRIVE, cls.MOVERS_SUITE_ATTACHMENT,
                cls.COMPANYCAM, cls.SHOPIFY, cls.QUICKBASE,  cls.INTERCOM, cls.ZOHO_BOOKS, cls.QUICKBOOKS,
                cls.ZOHO_INVENTORY, cls.FOLLOWUPBOSS, cls.COPPER, cls.EGNYTE, cls.XERO, cls.GOOGLECALENDAR, cls.ONEDRIVE,
                cls.MICROSOFT_DYNAMICS, cls.XERO_PAYROLL, cls.HUBSPOT_ATTACHMENT, cls.MICROSOFT_DYNAMICS_SALES]

    @classmethod
    def get_integration_names_that_support_redirection(cls):
        return [cls.INTERCOM]

    @classmethod
    def get_all_custom_integration_names(cls):
        return [cls.SHAG_CARPET]

    @classmethod
    def get_all_payment_integration_names(cls):
        return [cls.SQUARE, cls.QUICKBOOKS, cls.XERO]

    @classmethod
    def get_all_non_data_fetch_module_integration_names(cls):
        return [cls.PIPEDRIVE, cls.ZOHO, cls.HUBSPOT, cls.SALESFORCE, cls.SHOPIFY, cls.GOOGLECALENDAR]

    @classmethod
    def get_all_integration_names_that_support_forms(cls):
        return [cls.MOVERS_SUITE]
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
                cls.COMPANYCAM, cls.SHOPIFY, cls.QUICKBASE,  cls.INTERCOM, cls.ZOHO_BOOKS, cls.QUICKBOOKS,
                cls.ZOHO_INVENTORY, cls.FOLLOWUPBOSS, cls.COPPER, cls.EGNYTE, cls.XERO, cls.GOOGLECALENDAR, cls.ONEDRIVE,
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

def convert_integration_type_to_name(integration_type):
    if integration_type == ExternalIntegrationType.SAMSARA:
        return ExternalIntegrationName.SAMSARA
    elif integration_type == ExternalIntegrationType.MOVERBASE:
        return ExternalIntegrationName.MOVERBASE
    elif integration_type == ExternalIntegrationType.CURRENT_RMS:
        return ExternalIntegrationName.CURRENT_RMS
    elif integration_type == ExternalIntegrationType.VONIGO:
        return ExternalIntegrationName.VONIGO
    elif integration_type == ExternalIntegrationType.MOVERS_SUITE:
        return ExternalIntegrationName.MOVERS_SUITE
    elif integration_type == ExternalIntegrationType.PIPEDRIVE:
        return ExternalIntegrationName.PIPEDRIVE
    elif integration_type == ExternalIntegrationType.CALENDLY:
        return ExternalIntegrationName.CALENDLY
    elif integration_type == ExternalIntegrationType.HUBSPOT:
        return ExternalIntegrationName.HUBSPOT
    elif integration_type == ExternalIntegrationType.ZOHO:
        return ExternalIntegrationName.ZOHO
    elif integration_type == ExternalIntegrationType.SALESFORCE:
        return ExternalIntegrationName.SALESFORCE
    elif integration_type == ExternalIntegrationType.INFUSIONSOFT:
        return ExternalIntegrationName.INFUSIONSOFT
    elif integration_type == ExternalIntegrationType.MOVERS_SUITE_VENDOR_CONNECT:
        return ExternalIntegrationName.MOVERS_SUITE_VENDOR_CONNECT
    elif integration_type == ExternalIntegrationType.WORKDAY:
        return ExternalIntegrationName.WORKDAY
    elif integration_type == ExternalIntegrationType.SHAG_CARPET:
        return ExternalIntegrationName.SHAG_CARPET
    elif integration_type == ExternalIntegrationType.ACTIVECAMPAIGN:
        return ExternalIntegrationName.ACTIVECAMPAIGN
    elif integration_type == ExternalIntegrationType.SQUARE:
        return ExternalIntegrationName.SQUARE
    elif integration_type == ExternalIntegrationType.GOOGLEDRIVE:
        return ExternalIntegrationName.GOOGLEDRIVE
    elif integration_type == ExternalIntegrationType.GOOGLECALENDAR:
        return ExternalIntegrationName.GOOGLECALENDAR
    elif integration_type == ExternalIntegrationType.MOVERS_SUITE_ATTACHMENT:
        return ExternalIntegrationName.MOVERS_SUITE_ATTACHMENT
    elif integration_type == ExternalIntegrationType.COMPANYCAM:
        return ExternalIntegrationName.COMPANYCAM
    elif integration_type == ExternalIntegrationType.SHOPIFY:
        return ExternalIntegrationName.SHOPIFY
    elif integration_type == ExternalIntegrationType.QUICKBASE:
        return ExternalIntegrationName.QUICKBASE
    elif integration_type == ExternalIntegrationType.INTERCOM:
        return ExternalIntegrationName.INTERCOM
    elif integration_type == ExternalIntegrationType.ZOHO_BOOKS:
        return ExternalIntegrationName.ZOHO_BOOKS
    elif integration_type == ExternalIntegrationType.QUICKBOOKS:
        return ExternalIntegrationName.QUICKBOOKS
    elif integration_type == ExternalIntegrationType.ZOHO_INVENTORY:
        return ExternalIntegrationName.ZOHO_INVENTORY
    elif integration_type == ExternalIntegrationType.FOLLOWUPBOSS:
        return ExternalIntegrationName.FOLLOWUPBOSS
    elif integration_type == ExternalIntegrationType.COPPER:
        return ExternalIntegrationName.COPPER
    elif integration_type == ExternalIntegrationType.EGNYTE:
        return ExternalIntegrationName.EGNYTE
    elif integration_type == ExternalIntegrationType.XERO:
        return ExternalIntegrationName.XERO
    elif integration_type == ExternalIntegrationType.ONEDRIVE:
        return ExternalIntegrationName.ONEDRIVE
    elif integration_type == ExternalIntegrationType.MICROSOFT_DYNAMICS:
        return ExternalIntegrationName.MICROSOFT_DYNAMICS
    elif integration_type == ExternalIntegrationType.XERO_PAYROLL:
        return ExternalIntegrationName.XERO_PAYROLL
    elif integration_type == ExternalIntegrationType.HUBSPOT_ATTACHMENT:
        return ExternalIntegrationName.HUBSPOT_ATTACHMENT
    elif integration_type == ExternalIntegrationType.MICROSOFT_DYNAMICS_SALES:
        return ExternalIntegrationName.MICROSOFT_DYNAMICS_SALES
    else:
        return ''

class CRMServiceInfo(models.Model):
    crm_type = models.IntegerField(
        choices=[
            (ExternalIntegrationType.PIPEDRIVE,'Pipedrive'),
        ])
    crm_id = models.IntegerField  # deal_id of pipe_drive

    def serialize(self):
        return dict(
            crm_type=convert_integration_type_to_name(self.crm_type),
            crm_id=self.crm_id
        )
class PlanType:
    TEAM_MEMBERS = 1
    ENTERPRISE = 2

class RouteStartPoint:
    GROUP = 1001
    TASK = 1002

def convert_plan_type_to_text(type):
    if type == PlanType.TEAM_MEMBERS:
        return 'TEAM MEMBERS'
    elif type == PlanType.ENTERPRISE:
        return 'ENTERPRISE'
    else:
        return 'TEAM MEMBERS'

class InvitationChannelType:
    EMAIL = 3001
    SMS = 3002
    USERNAME = 30003

    @classmethod
    def get_all_invitation_channel_types(cls):
        return [cls.EMAIL, cls.SMS, cls.USERNAME]


DEFAULT_TASK_REMINDER_NOTIFICATION_TIME=-1
DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS=2
DEFAULT_RATING_TYPE='FiveStar'
DEFAULT_REVIEW_RESPONSE_DELAY=-1

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

    