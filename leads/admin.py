from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.UserProfile)
admin.site.register(models.Agent)
@admin.register(models.Lead)


class LeadsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'agent')