from django.http import HttpResponse, JsonResponse
import json
from utils import Util
import logging
from .models import ArrivyUser, UserProfile, EntityProfile, Entity, CompanyProfile
from signups.extraClasses import *


# Create your views here.

def signup(request):
    if request.method == 'POST':
        #t=Entity.objects.filter(owner__email='a@a.com')
        #print(t[0].pk)
        # tt=list(EntityProfile.objects.all())
        # for t in tt:
        #     print(t.user_companies.owned_company_id.email)
        # pp=list(Entity.objects.all())
        # for p in pp:
        #     print(p.owner.email)
        # user = ArrivyUser(username='abd1', email='a@a.com', first_name='ABD')
        # user.save()
        return HttpResponse('User Created')
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        email = ''
        if data.get('email') and data.get('email') != "":
            email = data.get('email')
            email = email.lower()
            email = Util.strip_email_address(email)
            if not Util.is_email_valid(email):
                return HttpResponse('Invalid Email', status=400)

        logging.info(f'Email is: {email}')

        plan = convert_plan_type_to_text(PlanType.TEAM_MEMBERS)
        plan_id = PlanType.TEAM_MEMBERS
        if data.get('is_enterprise'):
            if Util.check_if_true('is_enterprise', data.get('is_enterprise')):
                plan_id = PlanType.ENTERPRISE
                plan = convert_plan_type_to_text(PlanType.ENTERPRISE)

        is_premium_enabled = True
        if data.get('is_premium_enabled'):
            if Util.check_if_false('is_premium_enabled', data.get('is_premium_enabled')):
                is_premium_enabled = False

        entity_id = None
        if data.get('entity_id'):
            if not Util.check_if_integer('entity_id', data.get('entity_id')):
                return HttpResponse('Invalid entity_id', status=400)
            entity_id = int(data.get('entity_id'))

        signup_source = None
        if data.get('signup_source') and data.get('signup_source') != "":
            if not Util.check_if_string('signup_source', data.get('signup_source')):
                logging.info("signup_source is not string.")
                return HttpResponse("Invalid signup_source", 400)
            signup_source = data.get('signup_source')

        sso_access_token = None
        if data.get('sso_access_token') and data.request.get('sso_access_token') != "":
            if Util.check_attribute_type('sso_access_token', data.get('sso_access_token')) != 'string':
                logging.info("sso_access_token is not string.")
                return HttpResponse("Invalid access_token", status=400)
            sso_access_token = data.get('sso_access_token')

        sso_identification_key = None
        if data.get('sso_identification_key') and data.get('sso_identification_key') != "":
            if Util.check_attribute_type('sso_identification_key',
                                         data.get('sso_identification_key')) != 'string':
                logging.info("sso_identification_key is not string.")
                return HttpResponse("Invalid sso_identification_key", status=400)

            sso_identification_key = data.get('sso_identification_key')

        fullname = data.get('fullname')
        username = data.get('username')
        company_name = data.get('company_name')
        password = data.get('password')
        ref = data.get('ref')
        phone = data.get('phone')

    #register_user(email, password, fullname)
    return HttpResponse('User created')


# def register_user(email, password, request_fullname, ref, entity_id, send_verification_email_or_phone=True,
#                   phone=None, plan_id=PlanType.TEAM_MEMBERS, plan=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),
#                   request_company_name=None, custom_message_type=None, is_premium_enabled=True, username=None,
#                   verified=False, return_communication_data=False, signup_source=None, sso_access_token=None,
#                   sso_identification_key=None):
def register_user(email, password, request_fullname, verified=False):
    if request_fullname and not isinstance(request_fullname, str):
        fullname = str(request_fullname.encode('utf-8'))
    else:
        fullname = request_fullname

    # first we search that entity already exists we do so by searching the entity table
    # with the email in the request

    entity_already_exists=list(Entity.objects.filter(owner__email=email)) #fetching email

    if entity_already_exists:
        entity_already_exists=entity_already_exists[0]
        id_of_already_existing_entity=entity_already_exists.pk




    newuser = ArrivyUser(
        email=email,
        username=email,
        first_name=fullname,
        verified=verified,
        isCompany=True
    )
    newuser.set_password(password)
    newuser.save()

    notifications = dict(
        sms=True,
        email=True,
        mobile_notifications=True,
        desktop_notifications=True
    )
    allow_status_notifications = dict(
        ASSIGNED_TASKS_AND_ACTIVITIES=dict(title="Assigned Tasks & Activities", is_selected=False),
        OWN_PRIMARY_GROUP=dict(title="Own Primary Group", is_selected=False),
        OTHER_GROUPS=dict(title="Others Groups", is_selected=False),
        OTHERS=dict(title="Others", is_selected=False)
    )

    entity = Entity(
        owner=newuser,
        name=fullname,
        username=email,
        type="Company",
        is_default=True,
        email=email,
        group_id=None,
        notifications=notifications,
        allow_status_notifications=allow_status_notifications,
        user_type=convert_entity_user_name_to_type('CREW')
    )
    entity.save()

    profile = UserProfile(
        owner=newuser,
        fullname=fullname,
        company_owned=True,
        owned_company_id=1,
        company_entity_id=entity,
        default_entity_id=entity.pk,
        support_email=email,
        plan=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),
        plan_id=PlanType.TEAM_MEMBERS,
        status_priority=get_status_priorities(),
        signup_address="",
        signup_channel=InvitationChannelType.EMAIL,
    )
    profile.save()

    company_profile = CompanyProfile(
        owner=newuser,
        fullname=fullname,
        default_entity_id=entity.pk,
        support_email=email,
        # acquisition_source=ref,
        plan=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),
        plan_id=PlanType.TEAM_MEMBERS,
        status_priority=get_status_priorities(),
        # mobile_number=phone,
        signup_channel=InvitationChannelType.EMAIL,
        signup_address='',
        is_premium_enabled=True,
        is_test=False,
        is_company_verified=False,
        permission_groups_that_can_approve_crew_availability_requests=PERMISSION_GROUPS_THAT_CAN_APPROVE_CREW_AVAILABILITY_REQUESTS,
        sms_consent_provided=ConsentProvidedType.NO
    )

    # communication_data = []
    # if request_company_name and not isinstance(request_company_name, str):
    #     company_name = str(request_company_name.encode('utf-8'))
    # else:
    #     company_name = request_company_name
    #
    # good = False
    # registering_with_email = True
    # email_or_phone_or_username_use_for_registration = None
    # signup_channel = ''
    # signup_address = ''
    # is_test = False
    #
    # if email:
    #     logging.info('Verifying user registration data using email address')
    #     good = Util.verify_data(email=email, fullname=fullname, password=password)
    #     email_or_phone_or_username_use_for_registration = email
    #     signup_channel = InvitationChannelType.EMAIL
    #     signup_address = email
    #     is_test = Util.check_if_email_is_test(email)
    #     if is_test:
    #         logging.info(u'testing email domain found for signup against email: {}'.format(email))
    #
    # if phone:
    #     logging.info('Verifying user registration data using phone number')
    #     good = Util.verify_data(phone=phone, fullname=fullname, password=password)
    #     email_or_phone_or_username_use_for_registration = phone
    #     registering_with_email = False
    #     signup_channel = InvitationChannelType.SMS
    #     signup_address = phone
    #
    # if username:
    #     logging.info('Verifying user registration data using username')
    #     good = Util.verify_data(username=username, fullname=fullname, password=password)
    #     email_or_phone_or_username_use_for_registration = username
    #     signup_channel = InvitationChannelType.USERNAME
    #     signup_address = username
    #
    # if not good:
    #     return {}, 400, dict(
    #         message="MISSING_REQUEST_INFO",
    #         description='Data is invalid or missing'
    #     )
    #
    # if not password:
    #     # If no password is provided then most probable case is that signup is being done via SSO
    #     logging.info('Signup via SSO')
    #
    # invitations = None
    # entity_already_exists = None
    # id_of_already_existing_entity = None
    # owner_of_already_existing_entity = None
    # old_entity_user = None
    # company_profile = None
    # user_type = 'CREW'

    # if entity_id:
    #     logging.info("Checking if entity exists against provided entity_id: {} and using "
    #                  "it's phone, email and username".format(entity_id))
    #
    #     # entity_already_exists = Entity.get_by_id(entity_id)
    #
    #     email = entity_already_exists.email if (not email and entity_already_exists and
    #                                             hasattr(entity_already_exists, 'email') and
    #                                             entity_already_exists.email) else email
    #
    #     phone = entity_already_exists.phone if (not phone and entity_already_exists and
    #                                             hasattr(entity_already_exists, 'phone') and
    #                                             entity_already_exists.phone) else phone
    #
    #     username = entity_already_exists.username if (entity_already_exists and
    #                                                   hasattr(entity_already_exists, 'username') and
    #                                                   entity_already_exists.username) else username
    #
    #     # invitations = Invitation.by_entity(entity_id).fetch()
    #
    # if email and not entity_already_exists:
    #     logging.info(u"Checking if entity exists against provided email: {} and using "
    #                  u"it's phone and username".format(email))
    #
    #     # entity_already_exists = Entity.by_email(email).get()
    #
    #     phone = entity_already_exists.phone if (entity_already_exists and
    #                                             hasattr(entity_already_exists, 'phone') and
    #                                             entity_already_exists.phone) else phone
    #
    #     username = entity_already_exists.username if (entity_already_exists and
    #                                                   hasattr(entity_already_exists, 'username') and
    #                                                   entity_already_exists.username) else username
    #
    # if phone and not entity_already_exists:
    #     logging.info(u"Checking if entity exists against provided phone: {} and using "
    #                  u"it's email and username".format(phone))
    #
    #     # entity_already_exists = Entity.by_phone(phone).get()
    #
    #     email = entity_already_exists.email if (entity_already_exists and
    #                                             hasattr(entity_already_exists, 'email') and
    #                                             entity_already_exists.email) else email
    #
    #     username = entity_already_exists.username if (entity_already_exists and
    #                                                   hasattr(entity_already_exists, 'username') and
    #                                                   entity_already_exists.username) else username
    #
    # if username and not entity_already_exists:
    #     logging.info(u"Checking if entity exists against provided username: {} and using "
    #                  u"it's email and phone".format(username))
    #
    #     # entity_already_exists = Entity.by_username(username).get()
    #
    #     email = entity_already_exists.email if (entity_already_exists and
    #                                             hasattr(entity_already_exists, 'email') and
    #                                             entity_already_exists.email) else email
    #
    #     phone = entity_already_exists.phone if (entity_already_exists and
    #                                             hasattr(entity_already_exists, 'phone') and
    #                                             entity_already_exists.phone) else phone
