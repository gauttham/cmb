from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Snippet)


# For CMB

admin.site.register(models.ServiceClass)
admin.site.register(models.DedicatedAccount)
admin.site.register(models.ExceptionList)
admin.site.register(models.PrepaidInCdr)
admin.site.register(models.DaInCdrMap)

