from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    """
    User admin class
    """

    # The forms to add and change user instances
    form = UserAdminChangeForm  # edit
    add_form = UserAdminCreationForm  # create

    search_fields = ["id", "name"]
    ordering = ["id"]
    list_display = ["id", "name"]
    list_filter = ["id"]
    fieldsets = (
        (None, {"fields": ("id", "password")}),
        ("Personal info", {"fields": ("name",)}),
        ("Permissions", {"fields": ("admin",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("id", "password1", "password2")}),
    )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
