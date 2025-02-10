from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.services import (
    get_path_upload_avatar,
    validate_size_avatar,
    validate_phone_number
)


class ProfileUser(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    phone = models.CharField(
        _('phone number'),
        max_length=11,
        blank=True,
        null=True,
        unique=True,
        validators=[
            validate_phone_number,
            MinLengthValidator(11)
        ]
    )

    bio = models.TextField(
        _('biography'),
        blank=True,
        max_length=1000,
        help_text=_('Tell us about yourself (max 1000 characters)')
    )

    avatar = models.ImageField(
        _('avatar'),
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_size_avatar
        ],
        help_text=_('Upload your profile picture. Allowed formats: JPG, JPEG, PNG. Max size: 2MB.')
    )

    date_of_birth = models.DateField(
        _('date of birth'),
        blank=True,
        null=True
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.phone:
            self.phone = self.phone.strip().replace(' ', '')
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()
