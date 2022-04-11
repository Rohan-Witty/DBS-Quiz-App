from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .forms import UserAdminCreationForm, UserAdminChangeForm
# from .models import User
User = get_user_model()


admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm #edit
    add_form = UserCreationForm #create

    search_fields = ['id', 'name']
    ordering = ['id']
    list_display = ['id','name']
    list_filter = ['id']
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'password1', 'password2')}
        ),
    )
    filter_horizontal = ()

admin.site.register(User, UserAdmin)