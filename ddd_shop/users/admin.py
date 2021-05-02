from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from ddd_shop.users.models import *
from ddd_shop.users.forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (_("Permissions"), {"fields": ("is_active",
                                       "is_owner",
                                       "is_attendant",
                                       "groups",
                                       "user_permissions",
                                       ),
                            },),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]

class StoreOwnerAdmin(admin.ModelAdmin):
    model = StoreOwner
    list_display = ["user"]

class StoreAttendantAdmin(admin.ModelAdmin):
    model = StoreAttendant()
    list_display = ["user","shop"]


admin.site.register(User, UserAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(StoreAttendant,StoreAttendantAdmin)
admin.site.unregister(Group)
admin.site.register(Permission)
