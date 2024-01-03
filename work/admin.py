from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subcategories_count")
    search_fields = ("name",)

    def subcategories_count(self, obj):
        return obj.sub_categories.count()
    subcategories_count.short_description = _("Subcategory count")


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "works_count",
                    "workers_count", "employers_count")
    search_fields = ("name",)
    list_filter = ("category", )

    def works_count(self, obj):
        return obj.works.count()
    works_count.short_description = _("Ishlar soni")

    def workers_count(self, obj):
        return obj.users.filter(role="worker").count()
    workers_count.short_description = _("Ishchilar soni")

    def employers_count(self, obj):
        return obj.users.filter(role="employer").count()
    employers_count.short_description = _("Ish beruvchilar soni")


@admin.register(models.Work)
class Work(admin.ModelAdmin):
    list_display = ("id", "title", "status", "employer",
                    "subcategory", "region", "district", "worker", "created_at")
    list_filter = ("region", "district", "status", "subcategory")
    search_fields = ("title", "employer__full_name",)
    ordering = ("-created_at", "subcategory")
