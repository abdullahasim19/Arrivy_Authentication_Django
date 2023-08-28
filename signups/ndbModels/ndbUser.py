from google.cloud import ndb
import json


class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class ObjectProperty(ndb.BlobProperty):
    def _to_base_type(self, value):
        if isinstance(value, dict) or isinstance(value, AttributeDict):
            return json.dumps(value)
        else:
            return value

    def _from_base_type(self, value):
        if isinstance(value, str):
            try:
                return AttributeDict(json.loads(value))
            except:
                return value
        return value


class User(ndb.Model):
    email=ndb.StringProperty()
    password=ndb.StringProperty()
    name=ndb.StringProperty()
    auth_token = ndb.StringProperty()
    settings = ObjectProperty()
    is_disabled = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    is_company = ndb.BooleanProperty(default=False)
    profile_key = ndb.KeyProperty()
    # QR_String saved in the User model attribute will always have username_prefix.
    qr_code = ndb.StringProperty()

    # Adding ignored_auth_ids attribute to hide auth_ids from exposing on the UI which needs to be hidden like qr_code
    ignored_auth_ids = ndb.StringProperty(repeated=True)

    # To restrict a User to login via SSO only
    sso_only = ndb.BooleanProperty(default=False)

    def user_id(self):
        return str(self._key.id())

    def is_authenticated(self):
        return True