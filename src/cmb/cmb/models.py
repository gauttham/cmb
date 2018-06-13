from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from . import settings
from django.utils import timezone
from django.conf import settings as dsettings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=dsettings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class ServiceClass(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    isRevenueShare = models.BooleanField(default=False, db_index=True)
    inMobilesPercentage = models.IntegerField(null=True, default=50, db_index=True)
    otherOperatorPercentage = models.IntegerField(null=True, default=50)
    createdDate = models.DateTimeField(default=timezone.now, db_index=True)
    updatedDate = models.DateTimeField(auto_now=True, db_index=True)
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
    msisdn = models.CharField(primary_key=True, max_length=20, db_index=True)
    msisdnType = models.ForeignKey(msisdnType, on_delete=models.CASCADE, db_index=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.msisdn, self.msisdnType)


class InCdr(models.Model):
    id = models.AutoField(primary_key=True, max_length=20)
    serviceClass = models.ForeignKey(ServiceClass, on_delete=models.CASCADE, db_index=True, null=True)
    accountValueBeforeCall = models.FloatField(null=True)
    accountValueAfterCall = models.FloatField(null=True)
    callCharge = models.FloatField(null=True)
    chargedDuration = models.IntegerField(null=True)
    callStartTime = models.DateTimeField(db_index=True, null=True, blank=True)
    callerNumber = models.CharField(max_length=20, null=True, db_index=True)
    calledNumber = models.CharField(max_length=20, null=True, db_index=True)
    NCR = models.CharField(max_length=50, null=True, blank=True)
    subscriberType = models.IntegerField(default=1, db_index=True)
    redirectingNumber = models.CharField(null=True, blank=True, max_length=20)
    gsmCallRefNumber = models.CharField(max_length=20, null=True, blank=True)
    presentationIndicator = models.IntegerField(null=True)
    revenueShared = models.FloatField(null=True, blank=True)
    MICRevenue = models.FloatField(null=True, blank=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.serviceClass)


class beepCDR(models.Model):
    calledNumber = models.CharField(max_length=20, db_index=True)
    callerNumber = models.CharField(max_length=20, db_index=True)
    callStartTime = models.DateTimeField(db_index=True)
    MCID = models.CharField(max_length=20, null=True, blank=True)
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
    category = models.CharField(max_length=50, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=50, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s: %s: %s: %s' % (self.id, self.BeepToCallGap, self.isActive, self.category, self.timeDuration)


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
    InCdr = models.ForeignKey(InCdr, on_delete=models.CASCADE, related_name='dedicatedAccounts', null=True, blank=True)
    dedicatedAccount = models.IntegerField(null=True, blank=True, db_index=True)
    valueBeforeCall = models.FloatField(null=True, blank=True)
    valueAfterCall = models.FloatField(null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s: %s: %s' % (self.InCdr, self.DedicatedAccount, self.valueBeforeCall, self.valueAfterCall)


class ScheduleMgr(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    endPoint = models.CharField(max_length=240, blank=True, null=True)
    nextRunTime = models.DateTimeField()
    lastRunTime = models.DateTimeField()
    interval = models.IntegerField()
    lastReport = models.FileField(upload_to="../reports/", null=True, blank=True)
    lastRunStatus = models.CharField(max_length=20, default='Successful')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    createdBy = models.CharField(max_length=240, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=240, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s: %s : %s' % (self.name, self.nextRunTime, self.lastRunStatus, self.interval)

class testModel(models.Model):
    name = models.CharField(max_length=10, default='gautam')

    def __str__(self):
        return '%s' % self.name


class BulkLoadHistory(models.Model):
    type = models.CharField(max_length=50)
    initialCount = models.IntegerField()
    status = models.CharField(max_length=20)
    errorCount = models.IntegerField(null=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    uploadedBy = models.CharField(max_length=50)

    def __str__(self):
        return '%s; %s' % (self.type, self.uploadedBy)


class BulkLoadFailedList(models.Model):
    BulkLoadHistory = models.ForeignKey(BulkLoadHistory, on_delete=models.CASCADE)
    cdr = models.TextField(null=True)
    error = models.CharField(max_length=250)
    createdDate = models.DateTimeField(default=timezone.now)
    uploadedBy = models.CharField(max_length=50)

    def __str__(self):
        return '%s: %s' % (self.cdr, self.error)


class Roles(models.Model):
    roleName = models.CharField(max_length=50)
    createdBy = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.roleName


class userRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(to=Roles, blank=True)

    def __str__(self):
        return '%s' % (self.user)


class revenueCalculation(models.Model):
    subscriberType = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()

    def __str__(self):
        return "%s: %s" .format(self.subscriberType, self.status)

