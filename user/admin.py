from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django_celery_beat.models import CrontabSchedule, SolarSchedule, IntervalSchedule, ClockedSchedule, PeriodicTask
from django_celery_results.models import TaskResult, GroupResult
from rest_framework.authtoken.models import TokenProxy

from .models import CustomUser

# Register your models here.

admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(TaskResult)
admin.site.unregister(GroupResult)
admin.site.unregister(PeriodicTask)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(SocialApp)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)

admin.site.unregister(CrontabSchedule)
admin.site.unregister(SolarSchedule)
admin.site.unregister(IntervalSchedule)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'created_at', 'updated_at']
    fieldsets = None
