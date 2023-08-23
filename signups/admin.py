from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile,ArrivyUser,Entity,CompanyProfile,EntityProfile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets, (
            'Arrivy Info',
            {
                'fields': (
                    'settings_user',
                    'isdisabled',
                    'created',
                    'updated',
                    'isCompany',
                    'qr_code',
                    'ignored_auth_ids',
                    'sso_only',
                    'verified'
                )
            }
        )
    )


admin.site.register(ArrivyUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Entity)
admin.site.register(CompanyProfile)
admin.site.register(EntityProfile)
