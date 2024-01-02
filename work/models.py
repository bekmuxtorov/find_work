from django.db import models
from account.models import User, District, Region
from django.utils.translation import gettext_lazy as _


WORK_STATUS = (
    ("open", _("Ochiq")),
    ("closed", _("Yopiq")),
    ("waiting", _("Kutish")),
)


class Category(models.Model):
    name = models.CharField(
        verbose_name=_("Kategoriya"),
        max_length=100
    )

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="sub_categories"
    )
    name = models.CharField(
        verbose_name=_("SubCategory"),
        max_length=100
    )

    def __str__(self):
        return " | ".join([self.name, self.category.name])


class Work(models.Model):
    employer = models.ForeignKey(
        verbose_name=_("Ish beruvchi"),
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name=_("Ish nomi"),
        blank=True,
        null=True
    )
    subcategory = models.ForeignKey(
        to=SubCategory,
        verbose_name=_("SubCategory"),
        related_name="works",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    region = models.ForeignKey(
        to=Region,
        verbose_name=_("Viloyat"),
        related_name="works",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    district = models.ForeignKey(
        to=District,
        verbose_name=_("Tuman"),
        related_name="works",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name=_("Ish haqida batafsil")
    )
    status = models.CharField(
        verbose_name=_("Ish holati"),
        choices=WORK_STATUS,
        default="open",
        max_length=7
    )
    worker = models.ForeignKey(
        to=User,
        verbose_name=_("Olingan ishchi"),
        related_name="works",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("Yaratilgan vaqt"),
        auto_now_add=True
    )
    publish_date = models.DateTimeField(
        verbose_name=_("Chop etilgan vaqt")
    )

    def __str__(self):
        return " | ".join([self.employer.full_name, self.title])


"""
-- Works:
	employer(fk User)
	title
	subcategory
	region(fk Region)
	district(fk District)
	description
	created_at
	publish_date 
	status(closed/open/waiting)
	worker(fk User)
--  
"""
