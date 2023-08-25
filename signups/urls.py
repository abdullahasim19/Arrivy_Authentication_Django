from django.urls import path
from .views import login_user,signup,create_entity,logout_user

urlpatterns = [
    path('login',login_user),
    path('signup',signup),
    path('new_entity',create_entity),
    path('logout',logout_user)
]