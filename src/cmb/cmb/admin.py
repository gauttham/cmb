from django.contrib import admin

# Register your models here.
from . import models
import django_celery_beat

# For CMB

admin.site.register(models.ServiceClass)
admin.site.register(models.DedicatedAccount)
admin.site.register(models.ExceptionList)
admin.site.register(models.InCdr)
admin.site.register(models.DaInCdrMap)
admin.site.register(models.beepCDR)
admin.site.register(models.RevenueConfig)
admin.site.register(models.FreebiesType)
admin.site.register(models.Freebies)
admin.site.register(models.msisdnType)
admin.site.register(models.ScheduleMgr)


#####

# admin.site.register(django_celery_beat.models.CrontabSchedule)