from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.user.services import get_path_upload_avatar, validated_size_avatar, validated_phone_number


class ProfileUser(AbstractUser):
    phone = models.IntegerField(validators=[validated_phone_number], blank=True, null=True)
    bio = models.TextField(blank=True)
    logo = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validated_size_avatar]
    )
    print(phone)

    def __str__(self):
        return f'{self.email}'
