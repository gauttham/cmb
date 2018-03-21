from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from . import settings

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class ServiceClass(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.description)


class DedicatedAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100)
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s : %s :%s' % (self.id, self.product, self.type, self.sub_type)


class ExceptionList(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=100, db_index=True)
    type = models.CharField(max_length=50)
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s: %s' % (self.id, self.number, self.type)


class PrepaidInCdr(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    serviceClass = models.ForeignKey(ServiceClass, on_delete=models.CASCADE)
    accountValueBeforeCall = models.FloatField()
    accountValueAfterCall = models.FloatField()
    callCharge = models.FloatField()
    chargedDuration = models.IntegerField()
    callStartTime = models.DateTimeField()
    callerNumber = models.IntegerField()
    calledNumber = models.IntegerField()
    redirectingNumber = models.IntegerField(null=True)
    GsmCallRefNumber = models.CharField(max_length=100)
    presentationIndicator = models.IntegerField()
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.id, self.serviceClass)


class DaInCdrMap(models.Model):
    PrepaidInCdr = models.ForeignKey(PrepaidInCdr, on_delete=models.CASCADE)
    DedicatedAccount = models.ForeignKey(DedicatedAccount, on_delete=models.CASCADE)
    valueBeforeCall = models.FloatField()
    valueAfterCall = models.FloatField()
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s: %s: %s' % (self.PrepaidInCdr, self.DedicatedAccount, self.valueBeforeCall, self.valueAfterCall)


class beepCDR(models.Model):
    calledNumber = models.IntegerField()
    callerNumber = models.IntegerField()
    callStartTime = models.DateTimeField()
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)
    updatedBy = models.CharField(max_length=100, default=settings.DEFAULT_APP_USER)

    def __str__(self):
        return '%s: %s' % (self.calledNumber, self.callerNumber)

