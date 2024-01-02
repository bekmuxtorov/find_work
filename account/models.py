from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


USER_ROLE = (
    ("worker", _("Ishchi")),
    (("adminstrator"), _("Adminstrator")),
    (("employer"), _("Ish beruvchi"))
)


class Region(models.Model):
    name = models.CharField(_("Viloyat"), max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name=_("Tuman"),
        max_length=50
    )

    def __str__(self):
        return " | ".join([self.region, self.name])


class User(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(
        choices=USER_ROLE,
        max_length=12,
        verbose_name=_("User role")
    )
    phone_number = models.CharField(
        verbose_name=_("Telefon raqam"),
        max_length=20,
        unique=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message=_(
                    "Invalid phone number. Please enter in the format +998901234567")
            ),
        ]
    )
    full_name = models.CharField(
        verbose_name=_("FISH"),
        max_length=200
    )
    region = models.ForeignKey(
        to=Region,
        verbose_name=_("Viloyat"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    district = models.ForeignKey(
        to=District,
        verbose_name=_("Viloyat"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # subcategory(MM Subcategory)
    sms_code = models.CharField(
        verbose_name=_("sms code"),
        max_length=6,
        blank=True
    )
    is_phone_verified = models.BooleanField(
        verbose_name=_('Telefon tasdiqlangan'),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_("Bu ishchi"),
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name=_("Yaratilgan vaqt"),
        auto_now_add=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.phone_number