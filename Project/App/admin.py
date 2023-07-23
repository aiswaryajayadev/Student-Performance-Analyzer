from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from App.models import Customuser


class UserModel(UserAdmin):
    pass

admin.site.register(Customuser,UserModel)