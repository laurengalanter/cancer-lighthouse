from django.contrib import admin
from lighthouse.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import NullBooleanField
from django.forms.widgets import CheckboxInput
from django.forms import ModelForm, ValidationError
from django_admin_bootstrapped.admin.models import SortableInline

# Define an inline admin descriptor for Member model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
  model = LighthouseUser
  can_delete = False
  verbose_name_plural = 'lighthouse users'
    
  formfield_overrides = {
    NullBooleanField: {'widget': CheckboxInput},
  }

# Define a new User admin
class UserAdmin(UserAdmin):
  inlines = (UserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(FooModel, FooModelAdmin)

