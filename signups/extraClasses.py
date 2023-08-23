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


DEFAULT_TASK_REMINDER_NOTIFICATION_TIME=-1
DEFAULT_PENDING_REVIEW_REMINDER_ATTEMPTS=2
DEFAULT_RATING_TYPE='FiveStar'
DEFAULT_REVIEW_RESPONSE_DELAY=-1

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


class QRSettingsModesTypes:
    AUTO = 1001
    MANUAL = 1002
    MIGRATION = 1003
    NO_MODE = 1004

    @classmethod
    def get_all_qr_settings_modes_types(cls):
        return [QRSettingsModesTypes.AUTO, QRSettingsModesTypes.MANUAL, QRSettingsModesTypes.MIGRATION,
                QRSettingsModesTypes.NO_MODE]

