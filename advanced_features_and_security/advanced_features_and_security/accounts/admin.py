from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Extend Django admin to support custom user model fields.
    """

    model = CustomUser

    # Fields shown in list view
    list_display = ("username", "email", "date_of_birth", "is_staff")

    # Fields available in the edit page
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info", {
                "fields": ("date_of_birth", "profile_photo")
            }
        ),
    )

    # Fields available when creating a user from admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Info", {
                "fields": ("date_of_birth", "profile_photo")
            }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
