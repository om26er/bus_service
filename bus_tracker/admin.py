from django.contrib import admin

from bus_tracker.models import DriverModel


class UserProfileAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'userprofile'

admin.site.register(DriverModel, UserProfileAdmin)
