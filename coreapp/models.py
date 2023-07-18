import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_class


# Create your models here.

class UserTypeChoice(models.TextChoices):
    PROF = "PROFESSOR", "Staff"
    STUD = "STUDENT", "Student"


UniversityDepartment = get_class('address.models', 'UniversityDepartment')


class User(AbstractUser):
    name = models.CharField(verbose_name='Display Name', max_length=100, null=True, blank=True)
    is_new_user = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    no_email = models.BooleanField(default=False)
    is_profile_complete = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10, choices=UserTypeChoice.choices, default=UserTypeChoice.STUD, verbose_name='User Status')
    department = models.ForeignKey(to=UniversityDepartment, on_delete=models.PROTECT, null=True)

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.user_type == UserTypeChoice.PROF and self.department is None:
            raise ValidationError({'department': _('Department can not be empty if user is not a student.')})
        # Set the pub_date for published items if it hasn't been set already.

    # @property
    # def get_full_name(self):

    class Meta:
        permissions = [
            ('can_view_oms', 'Can view OMS portal'),
        ]
