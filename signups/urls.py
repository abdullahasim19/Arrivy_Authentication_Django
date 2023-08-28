from django.urls import path
from .views import login_user, signup, create_entity, logout_user
from .cloudViews import signup_ndb, create_entity_ndb, login_ndb

urlpatterns = [
    # sqlite routes
    path('login', login_user),
    path('signup', signup),
    path('new_entity', create_entity),
    path('logout', logout_user),

    # cloud ndb routes
    path('ndb_signup', signup_ndb),
    path('ndb_new_entity', create_entity_ndb),
    path('ndb_login', login_ndb)

]
