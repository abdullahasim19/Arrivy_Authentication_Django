from django.http import HttpResponse, JsonResponse
from .ndbModels import CompanyProfile, Entity, EntityProfile, UserProfile, User, UserCompany
from google.cloud import ndb
import os
import logging
from .extraClasses import *
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"


def create_entity_ndb(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    email = data.get('email')
    name = data.get('fullname')
    password = data.get('password')

    client = ndb.Client()
    # if ndb.get_context():
    #     ndb.get_context().clear_cache()
    with client.context():
        o = User.query(User.email == 'a@arrivy.com').get()
        i = int(o.user_id())
        e = Entity(owner=i, email=email, name=name)
        e.put()

    register_user(email, password, name)

    return HttpResponse('Entity Created')


def register_user(email, password, request_fullname):
    if request_fullname and not isinstance(request_fullname, str):
        fullname = str(request_fullname.encode('utf-8'))
    else:
        fullname = request_fullname

    client = ndb.Client()
    # context = client.context()
    with client.context():
        entity_already_exists = None
        id_of_already_existing_entity = None
        owner_of_already_existing_entity = None
        company_profile = None
        entity_already_exists = Entity.by_email(email).get()

        if entity_already_exists:
            id_of_already_existing_entity = entity_already_exists.get_id()
            owner_of_already_existing_entity = entity_already_exists.owner

            old_entity_profile = EntityProfile.query(
                EntityProfile.user_companies.company_entity_id == id_of_already_existing_entity).get()
            if not old_entity_profile:  # if no entity profile is found we search for
                old_entity_profile = CompanyProfile.query(
                    CompanyProfile.default_entity_id == id_of_already_existing_entity).get()

            if old_entity_profile:
                old_entity_user = ndb.Key('User', old_entity_profile.owner).get()

            if not company_profile:
                company_profile = CompanyProfile.by_user(owner_of_already_existing_entity).get()

        # if entity_already_exists and email:
        #     existing_user_found = False
        #     # if a user with same email exists within company
        #     # finding users of same company
        #     existing_users_within_company = EntityProfile.query(
        #         EntityProfile.user_companies.owned_company_id == owner_of_already_existing_entity).fetch()  # different users working for same owner
        #     for existing_user_within_company in existing_users_within_company:
        #         for existing_user_within_company_user_company in existing_user_within_company.user_companies:
        #             if existing_user_within_company_user_company.owned_company_id == owner_of_already_existing_entity and \
        #                     existing_user_within_company_user_company.signup_address == email and \
        #                     existing_user_within_company_user_company.company_entity_id != id_of_already_existing_entity:
        #                 logging.info('Entity profile already exists with same email')
        #                 existing_user_found = True

        # Sequence of extra property names that must be unique.
        # unique_properties = []
        # if email:
        #     unique_properties.append('email')

        user = User(email=email, name=fullname, password=password)
        user.put()
        user_id = int(user.user_id())

        company_owned = False
        owned_company_id = None
        company_entity_id = None
        default_entity_id = None

        if entity_already_exists:
            logging.info("Entity already exists")
            company_owned = True
            owned_company_id = owner_of_already_existing_entity
            company_entity_id = id_of_already_existing_entity
        else:
            logging.info("Creating new Entity")
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
                owner=user_id,
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
            entity.put()
            entity_id = entity.get_id()
            default_entity_id = entity_id

        profile = UserProfile(
            owner=user_id,
            fullname=fullname,
            company_owned=True,
            owned_company_id=owned_company_id,
            company_entity_id=company_entity_id,
            default_entity_id=default_entity_id,
            support_email=email,
            plan=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),
            plan_id=PlanType.TEAM_MEMBERS,
            status_priority=get_status_priorities(),
            signup_address=email,
            signup_channel=InvitationChannelType.EMAIL,
        )
        profile.put()

        if company_owned:
            user_company = UserCompany(
                owned_company_id=owned_company_id,
                company_entity_id=company_entity_id,
                signup_address=email,
                signup_channel=InvitationChannelType.EMAIL,
            )
            logging.info('Creating Entity Profile')
            entity_profile = EntityProfile(
                owner=user_id,
                fullname=fullname,
                owned_company_id=owned_company_id,
                company_entity_id=company_entity_id,
                email=email,
                user_companies=[user_company]
            )
            entity_profile.put()
        else:
            logging.info('Creating Company Profile')
            company_profile = CompanyProfile(
                owner=user_id,
                fullname=fullname,
                default_entity_id=default_entity_id,
                support_email=email,
                plan=convert_plan_type_to_text(PlanType.TEAM_MEMBERS),
                plan_id=PlanType.TEAM_MEMBERS,
                status_priority=get_status_priorities(),
                signup_channel=InvitationChannelType.EMAIL,
                signup_address=email,
                is_premium_enabled=True,
                is_test=False,
                is_company_verified=False,
                permission_groups_that_can_approve_crew_availability_requests=PERMISSION_GROUPS_THAT_CAN_APPROVE_CREW_AVAILABILITY_REQUESTS,
                sms_consent_provided=ConsentProvidedType.NO
            )
            company_profile.put()
    # context.__exit__(None, None, None)


def signup_ndb(request):
    if request.method != 'POST':
        return HttpResponse('Error')
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    email = data.get('email')
    password = data.get('password')
    fullname = data.get('fullname')

    register_user(email, password, fullname)
    return HttpResponse('USER CREATED')


def testing(request):
    client = ndb.Client()
    with client.context():
        pass
    return HttpResponse('Hello world')