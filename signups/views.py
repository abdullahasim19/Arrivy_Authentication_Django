from django.http import HttpResponse, JsonResponse
import json
from utils import Util
import logging
from .models import ArrivyUser, UserProfile, EntityProfile, Entity, CompanyProfile, UserCompany
from signups.extraClasses import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.


def logout_user(request):
    if not request.user.is_authenticated:
        return HttpResponse('User already logged out')
    logout(request)
    return HttpResponse('USER LOGGED OUT')


@login_required
def create_entity(request):
    if request.method!='POST':
        return HttpResponse('Error')
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    email = data.get('email')
    name = data.get('fullname')
    password=data.get('password')
    ##t=request.user
    ##print(type(t))
    ##return HttpResponse('hello')
    company_id=request.user
    ##company_id = ArrivyUser.objects.get(username='test@arrivy.com')  # later we will fetch the authenticated user
    entity = Entity(
        owner=company_id,
        name=name,
        email=email
    )
    entity.save()
    register_user(email,password,name)
    return HttpResponse('Entity Created')


def login_user(request):
    if request.method=="POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        email=data.get("email")
        password=data.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return HttpResponse('LOGIN DONE')
        else:
            return HttpResponse('LOGIN FAILED',status=401)

    return HttpResponse('ERROR',status=400)


def signup(request):
    if request.method == 'POST':
        # t=Entity.objects.filter(owner__email='a@a.com')
        # print(t[0].pk)
        # tt=list(EntityProfile.objects.all())
        # for t in tt:
        #     print(t.user_companies.owned_company_id.email)
        # pp=list(Entity.objects.all())
        # for p in pp:
        #     print(p.owner.email)
        # user=ArrivyUser.objects.all()
        # for u in user:
        #     print(f'{u.username} {u.pk}')
        # try:
        #     e = EntityProfile.objects.get(user_companies__owned_company_id__pk=10)
        #     print(e)
        # except Exception as e:
        #     print(e)

        # user = ArrivyUser( username='abdullah',email='abdullah.asim@arrivy.com', first_name='Abdullah')
        # user.set_password('12345')
        # user.save()
        ##return HttpResponse('User Created')
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # email = ''
        # if data.get('email') and data.get('email') != "":
        #     email = data.get('email')
        #     email = email.lower()
        #     email = Util.strip_email_address(email)
        #     if not Util.is_email_valid(email):
        #         return HttpResponse('Invalid Email', status=400)
        #
        # logging.info(f'Email is: {email}')
        #
        # plan = convert_plan_type_to_text(PlanType.TEAM_MEMBERS)
        # plan_id = PlanType.TEAM_MEMBERS
        # if data.get('is_enterprise'):
        #     if Util.check_if_true('is_enterprise', data.get('is_enterprise')):
        #         plan_id = PlanType.ENTERPRISE
        #         plan = convert_plan_type_to_text(PlanType.ENTERPRISE)
        #
        # is_premium_enabled = True
        # if data.get('is_premium_enabled'):
        #     if Util.check_if_false('is_premium_enabled', data.get('is_premium_enabled')):
        #         is_premium_enabled = False
        #
        # entity_id = None
        # if data.get('entity_id'):
        #     if not Util.check_if_integer('entity_id', data.get('entity_id')):
        #         return HttpResponse('Invalid entity_id', status=400)
        #     entity_id = int(data.get('entity_id'))
        #
        # signup_source = None
        # if data.get('signup_source') and data.get('signup_source') != "":
        #     if not Util.check_if_string('signup_source', data.get('signup_source')):
        #         logging.info("signup_source is not string.")
        #         return HttpResponse("Invalid signup_source", 400)
        #     signup_source = data.get('signup_source')
        #
        # sso_access_token = None
        # if data.get('sso_access_token') and data.request.get('sso_access_token') != "":
        #     if Util.check_attribute_type('sso_access_token', data.get('sso_access_token')) != 'string':
        #         logging.info("sso_access_token is not string.")
        #         return HttpResponse("Invalid access_token", status=400)
        #     sso_access_token = data.get('sso_access_token')
        #
        # sso_identification_key = None
        # if data.get('sso_identification_key') and data.get('sso_identification_key') != "":
        #     if Util.check_attribute_type('sso_identification_key',
        #                                  data.get('sso_identification_key')) != 'string':
        #         logging.info("sso_identification_key is not string.")
        #         return HttpResponse("Invalid sso_identification_key", status=400)
        #
        #     sso_identification_key = data.get('sso_identification_key')
        #
        # fullname = data.get('fullname')
        # username = data.get('username')
        # company_name = data.get('company_name')
        # password = data.get('password')
        # ref = data.get('ref')
        # phone = data.get('phone')
        email = data.get('email')
        password = data.get('password')
        fullname = data.get('fullname')
        register_user(email, password, fullname)
        return HttpResponse('USER CREATED')
    return HttpResponse('Users created')


def register_user(userEmail, password, request_fullname, verified=False):
    if request_fullname and not isinstance(request_fullname, str):
        fullname = str(request_fullname.encode('utf-8'))
    else:
        fullname = request_fullname

    # first we search that entity already exists we do so by searching the entity table
    # with the email in the request
    entity_already_exists = None
    try:
        entity_already_exists = Entity.objects.get(email=userEmail)  # fetching email
    except Exception as e:
        logging.error(e)

    id_of_already_existing_entity = None
    owner_of_already_existing_entity = None
    if entity_already_exists:
        id_of_already_existing_entity = entity_already_exists
        owner_of_already_existing_entity = entity_already_exists.owner
        user_type = convert_entity_user_type_to_name(entity_already_exists.user_type)

        old_entity_profile = None
        try:
            old_entity_profile = EntityProfile.objects.get(user_companies__company_entity_id
                                                           =id_of_already_existing_entity)
        except Exception as e:
            logging.error(e)

        if not old_entity_profile:  # if no entity profile is found we search for
            try:
                old_entity_profile = CompanyProfile.objects.get(default_entity_id=id_of_already_existing_entity)
            except Exception as e:
                logging.error(e)

        company_profile = None
        try:
            company_profile = CompanyProfile.objects.get(owner=owner_of_already_existing_entity)
        except Exception as e:
            logging.error(e)

    existing_users_within_company = None
    if entity_already_exists and userEmail:
        try:
            existing_users_within_company = list(EntityProfile.objects.
            filter(
                user_companies__owned_company_id=owner_of_already_existing_entity))
        except Exception as e:
            logging.error(e)

    # existing_user_found = None
    # for existing_user_within_company in existing_users_within_company:
    #     for existing_user_within_company_user_company in existing_user_within_company.user_companies:
    #         if existing_user_within_company_user_company.owned_company_id.pk == owner_of_already_existing_entity and \
    #                 existing_user_within_company_user_company.signup_address == userEmail and \
    #                 existing_user_within_company_user_company.company_entity_id.pk != id_of_already_existing_entity:
    #             logging.info('Entity profile already exists with same email')
    #             existing_user_found = True

    newUser = ArrivyUser(
        email=userEmail,
        username=userEmail,
        first_name=fullname,
        verified=verified,
        isCompany=True
    )
    newUser.set_password(password)
    newUser.save()

    default_entity_id = None
    owned_company_id = None
    company_entity_id = None
    company_owned = False
    if entity_already_exists:
        owned_company_id = owner_of_already_existing_entity
        company_entity_id = id_of_already_existing_entity
        company_owned = True
        logging.info('Entity Already Exists')
    else:
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
        # owner_user=ArrivyUser.objects.get(username='abdullah')
        entity = Entity(
            owner=newUser,
            name=fullname,
            username=userEmail,
            type="Company",
            is_default=True,
            email=userEmail,
            group_id=None,
            notifications=notifications,
            allow_status_notifications=allow_status_notifications,
            user_type=convert_entity_user_name_to_type('CREW')
        )
        entity.save()
        default_entity_id = entity
    # owner_user = ArrivyUser.objects.get(username='abdullah')
    logging.info('Creating User Profile')
    profile = UserProfile(
        owner=newUser,
        fullname=fullname,
        company_owned=True,
        owned_company_id=owned_company_id,
        company_entity_id=company_entity_id,
        default_entity_id=default_entity_id,
        support_email=userEmail,
        plan=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),
        plan_id=PlanType.TEAM_MEMBERS,
        status_priority=get_status_priorities(),
        signup_address=userEmail,
        signup_channel=InvitationChannelType.EMAIL,
    )
    profile.save()
    if company_owned:
        user_company = UserCompany(
            owned_company_id=owned_company_id,
            company_entity_id=company_entity_id,
            signup_address=userEmail,
            signup_channel=InvitationChannelType.EMAIL
        )
        user_company.save()
        logging.info('Creating Entity Profile')
        entity_profile = EntityProfile(
            owner=newUser,
            fullname=fullname,
            owned_company_id=owned_company_id,
            company_entity_id=company_entity_id,
            email=userEmail,
            user_companies=user_company
        )
        entity_profile.save()
    else:
        logging.info('Creating Company Profile')
        company_profile = CompanyProfile(
            owner=newUser,
            fullname=fullname,
            default_entity_id=default_entity_id,
            support_email=userEmail,
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
        company_profile.save()
    # return HttpResponse('User Created')

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
