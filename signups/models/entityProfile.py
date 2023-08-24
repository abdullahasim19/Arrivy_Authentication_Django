from django.db import models
from .entity import  Entity
from .userModel import ArrivyUser
from signups.extraClasses import *


class UserCompany(models.Model):
    owned_company_id = models.ForeignKey(ArrivyUser, on_delete=models.CASCADE)
    company_entity_id = models.ForeignKey(Entity, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(default=False)
    signup_channel = models.IntegerField(choices=[
        (InvitationChannelType.EMAIL, 'Email'),
        (InvitationChannelType.SMS, 'SMS'),
        (InvitationChannelType.USERNAME, 'Username')
    ], default=InvitationChannelType.EMAIL,blank=True,null=True)
    signup_address = models.CharField(max_length=100,blank=True,null=True)
    # Used in migration when Entity has both email and phone as a auth_ids.
    signup_channel_2 = models.IntegerField(choices=[
        (InvitationChannelType.EMAIL, 'Email'),
        (InvitationChannelType.SMS, 'SMS'),
        (InvitationChannelType.USERNAME, 'Username')
    ], default=InvitationChannelType.EMAIL,blank=True,null=True)
    signup_address_2 = models.CharField(max_length=100,blank=True,null=True)

    #  todo: remove this flag after we ran migrations
    is_disable = models.BooleanField(default=False)

    # user type will differentiate between customer and crew
    user_type = models.IntegerField(
        choices=[
            (EntityUserTypes.CUSTOMER, 'Customer'),
            (EntityUserTypes.CREW, 'Crew')
        ],
        default=EntityUserTypes.CREW)


class EntityProfile(models.Model):
    owner = models.ForeignKey(ArrivyUser,on_delete=models.CASCADE,blank=True,null=True) # should be foreign key from user
    address = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True,null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    emergency = models.CharField(max_length=100, blank=True, null=True)
    exact_location = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    image_id = models.IntegerField(blank=True,null=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)
    intro = models.CharField(max_length=100, blank=True, null=True)

    acquisition_source = models.CharField(max_length=100, blank=True, null=True)

    company_entity_id = models.IntegerField(models.ForeignKey(Entity,on_delete=models.CASCADE),blank=True,null=True)  # should be foreign key corresponding entity
    owned_company_id = models.IntegerField(models.ForeignKey(ArrivyUser,on_delete=models.CASCADE),blank=True,null=True)  # should be foreign key from User

    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    social_links = models.JSONField(blank=True,null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    user_companies = models.OneToOneField(UserCompany, on_delete=models.CASCADE)
    is_on_boarding_guide_visited = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
