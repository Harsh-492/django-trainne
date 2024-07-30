from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,PermissionsMixin
from .manager import CustomUserManager

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=True,null=True)
    is_active = models.BooleanField(default=True,null=True)
    is_superuser = models.BooleanField(default=False,null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []    

    objects = CustomUserManager()

    def __str__(self):
        return self.email

