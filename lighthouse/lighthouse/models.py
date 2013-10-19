from django.db.models import *
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey

class LighthouseUser(Model):
  user = OneToOneField(User)
  first_login = BooleanField(default=True, verbose_name='First login? ' +
    '(force user to reset password)')
  # must be nullable so save will work
  # cancer_type = ForeignKey(CancerType, null=True)
  # phone_number = CharField(max_length=15, blank=True, null=True)
  
