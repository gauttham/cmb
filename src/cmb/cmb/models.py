from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from . import settings
from django.utils import timezone

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class ServiceClass(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50)
    isRevenueShare = models.BooleanField(default=False)
    inMobilesPercentage = models.IntegerField(null=True, default=50)
    otherOperatorPercentage = models.IntegerField(null=True, default=50)
    createdDate = models.DateTimeField(default=timezone.now)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.description)


class msisdnType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)


class ExceptionList(models.Model):
    msisdn = models.CharField(primary_key=True, max_length=20)
    msisdnType = models.ForeignKey(msisdnType, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.msisdn, self.msisdnType)


class PrepaidInCdr(models.Model):
    id = models.AutoField(primary_key=True, max_length=20)
    serviceClass = models.ForeignKey(ServiceClass, on_delete=models.CASCADE)
    accountValueBeforeCall = models.FloatField()
    accountValueAfterCall = models.FloatField()
    callCharge = models.FloatField()
    chargedDuration = models.IntegerField()
    callStartTime = models.DateTimeField()
    callerNumber = models.CharField(max_length=20)
    calledNumber = models.CharField(max_length=20)
    subscriberType = models.IntegerField(default=1)
    redirectingNumber = models.CharField(null=True, blank=True, max_length=20)
    gsmCallRefNumber = models.CharField(max_length=20, null=True, blank=True)
    presentationIndicator = models.IntegerField()
    revenueShared = models.FloatField(null=True, blank=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.serviceClass)


class beepCDR(models.Model):
    calledNumber = models.CharField(max_length=20)
    callerNumber = models.CharField(max_length=20)
    callStartTime = models.DateTimeField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.calledNumber, self.callerNumber)


class RevenueConfig(models.Model):
    BeepToCallGap = models.IntegerField(default=60)  # in minutes
    isActive = models.BooleanField(default=False)
    timeDuration = models.IntegerField(default=30)  # This will run by default for the last 30 days worth of data

    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.BeepToCallGap, self.isActive)


class Freebies(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.Name)


class FreebiesType(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.Name)


class DedicatedAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=100)
    type = models.ForeignKey(Freebies, on_delete=models.CASCADE)
    sub_type = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s' % (self.id)


class DaInCdrMap(models.Model):
    PrepaidInCdr = models.ForeignKey(PrepaidInCdr, on_delete=models.CASCADE, related_name='dedicatedAccounts')
    dedicatedAccount = models.IntegerField(null=True, blank=True)
    valueBeforeCall = models.FloatField(null=True, blank=True)
    valueAfterCall = models.FloatField(null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s: %s: %s' % (self.PrepaidInCdr, self.DedicatedAccount, self.valueBeforeCall, self.valueAfterCall)

