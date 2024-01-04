from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

from .managers import UserManager


USER_ROLE = (
    ("worker", _("Ishchi")),
    ("adminstrator", _("Adminstrator")),
    ("employer", _("Ish beruvchi"))
)


class TokenProxy(Token):
    class Meta:
        proxy = True
        verbose_name = "Token"
        verbose_name_plural = "Tokens"


class Region(models.Model):
    name = models.CharField(_("Viloyat"), max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        related_name="districts",
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name=_("Tuman"),
        max_length=50
    )

    def __str__(self):
        return " | ".join([self.name, self.region.name])


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
        related_name="users",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    district = models.ForeignKey(
        to=District,
        verbose_name=_("Tuman"),
        related_name="users",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subcategory = models.ManyToManyField(
        to="work.SubCategory",
        related_name="users",
        blank=True,
    )
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
        verbose_name=_("Bu sayt ishchisi"),
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name=_("Yaratilgan vaqt"),
        auto_now_add=True
    )
    image = models.ImageField(
        verbose_name=_("Rasm"),
        upload_to='users/',
        default="users/default.jpg"
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.phone_number


class Employer(models.Model):
    full_name = models.CharField(
        verbose_name=_("FISH"),
        max_length=200
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
    created_at = models.DateTimeField(
        verbose_name=_("Yaratilgan vaqt"),
        auto_now_add=True
    )

    def __str__(self):
        return " | ".join([self.full_name, self.phone_number])
