from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
from . import forms

admin.site.site_header = _("Online Ishchi")
admin.site.index_title = 'Online Ishchi Administration'


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "districts_count",
                    "workers_count", "employers_count")
    search_fields = ("name",)

    def districts_count(self, obj):
        return obj.districts.count()
    districts_count.short_description = _("Tumanlar soni")

    def workers_count(self, obj):
        return obj.users.filter(role="worker").count()
    workers_count.short_description = _("Ishchilar soni")

    def employers_count(self, obj):
        return obj.users.filter(role="employer").count()
    employers_count.short_description = _("Ish beruvchilar soni")


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "region", "workers_count", "employers_count")
    search_fields = ("name",)
    list_filter = ("region",)

    def workers_count(self, obj):
        return obj.users.filter(role="worker").count()
    workers_count.short_description = _("Ishchilar soni")

    def employers_count(self, obj):
        return obj.users.filter(role="employer").count()
    employers_count.short_description = _("Ish beruvchilar soni")


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    list_display = (
        "phone_number",
        "role",
        "full_name",
        "region",
        "district",
        "created_at",
        "is_phone_verified",
        "is_staff"
    )
    list_filter = ("is_staff", "is_superuser",
                   "role", "region", "district")

    fieldsets = (
        (
            "General data",
            {
                "fields": (
                    "role",
                    "phone_number",
                )
            },
        ),
        (
            "User",
            {
                "fields": (
                    "full_name",
                    "region",
                    "district",
                    "image"
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser",
                        "groups", "user_permissions")},
        ),
        ("Important dates", {
         "fields": ("last_login", 'sms_code', 'is_phone_verified')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("role", "phone_number", "password1", "password2"),
            },
        ),
    )
    search_fields = ("phone_number", "full_name")
    ordering = ("role",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.type = form.cleaned_data.get('type')
        super().save_model(request, obj, form, change)
