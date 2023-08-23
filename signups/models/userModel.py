from django.db import models
from django.contrib.auth.models import AbstractUser
#from .entity import Entity
#from .entity import Entity
#from geoposition.fields import GeopositionField

class ArrivyUser(AbstractUser):
    settings_user=models.BinaryField(blank=True,null=True,editable=True)
    isdisabled=models.BooleanField(default=False,blank=True,null=True)
    created=models.DateTimeField(blank=True,null=True)
    updated=models.DateTimeField(blank=True,null=True)
    isCompany=models.BooleanField(default=False,blank=True,null=True)
    qr_code=models.CharField(blank=True,null=True,max_length=100)
    ignored_auth_ids=models.CharField(max_length=100,blank=True,null=True)
    sso_only=models.CharField(default=False,max_length=100,blank=True,null=True)
    verified=models.BooleanField(default=False)



