import base64
import os
import uuid
from datetime import datetime
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import IntegrityError, models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .manager import AppUserManager


class BaseTimeStampModel(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(BaseTimeStampModel, self).save(*args, **kwargs)

def generate_id():
    r_id = base64.b64encode(os.urandom(6)).decode('ascii')
    r_id = r_id.replace(
        '/', '').replace('_', '').replace('+', '').strip()
    return r_id


def usermanagerprofile(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '{0}_manager_profile_pic/{1}'.format(instance.username, filename)


class User(AbstractBaseUser, PermissionsMixin):
    OWNER = 'OWNER'
    CASHIER = 'CASHIER'
    KITCHEN = 'KITCHEN'
    DEV = 'DEVELOPER'
    types = (
        (OWNER,'OWNER'),
        (CASHIER,'CASHIER'),
        (KITCHEN,'KITCHEN'),
        (DEV,'DEV')
    )
    id = models.CharField(max_length=255, primary_key=True,
                          editable=False)
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length=20, null=True, blank=True, choices=types, default=DEV)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AppUserManager()

    def create_unique_username(self):
        strip = self.email.replace('@', '_').replace(
            '.com', '').replace('.', '_')
        unique_usr = "%s%s" % (uuid.uuid4().hex[:8], strip)
        return unique_usr

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
        if not self.id:
            self.id = generate_id()
            self.date_joined = timezone.now()
            if not self.username:
                self.username = self.create_unique_username()
            # using your function as above or anything else
            success = False
            failures = 0
            while not success:
                try:
                    super(User, self).save(*args, **kwargs)
                except IntegrityError:
                    failures += 1
                    if failures > 5:  # or some other arbitrary cutoff point at which things are clearly wrong
                        raise KeyError
                    else:
                        # looks like a collision, try another random value
                        self.id = generate_id()
                else:
                    success = True
        else:
            super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user_core'