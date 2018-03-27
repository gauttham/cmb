from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, ServiceClass, DedicatedAccount, ExceptionList, PrepaidInCdr, DaInCdrMap, beepCDR, RevenueConfig, Freebies, FreebiesType
from django.utils import timezone


class ServiceClassSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = ServiceClass
        fields = ('id', 'description', 'isRevenueShare', 'inMobilesPercentage',
                  'otherOperatorPercentage', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class DedicatedAccountSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = DedicatedAccount
        fields = ('id', 'product', 'type', 'sub_type', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class ExceptionListSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = ExceptionList
        fields = ('msisdn', 'msisdnType', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class DaInCdrMapSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    class Meta:
        model = DaInCdrMap
        fields = ('PrepaidInCdr', 'DedicatedAccount', 'valueBeforeCall', 'valueAfterCall',
                  'createdDate', 'updatedDate', 'createdBy', 'updatedBy')


class DaInCdrMapforInCDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaInCdrMap
        fields = ('DedicatedAccount', 'valueBeforeCall', 'valueAfterCall')


class PrepaidInCdrSerializer(serializers.ModelSerializer):
    callStartTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    dedicatedAccounts = DaInCdrMapforInCDRSerializer(many=True, read_only=True)

    class Meta:
        model = PrepaidInCdr
        fields = ('id', 'serviceClass', 'accountValueBeforeCall', 'accountValueAfterCall', 'callCharge',
                  'chargedDuration', 'callStartTime', 'callerNumber', 'calledNumber', 'redirectingNumber',
                  'gsmCallRefNumber', 'presentationIndicator', 'revenueShared', 'reason', 'dedicatedAccounts',
                  'createdDate', 'updatedDate', 'createdBy', 'updatedBy')


class beepCDRSerializer(serializers.ModelSerializer):
    callStartTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = beepCDR
        fields = ('calledNumber', 'callerNumber', 'callStartTime', 'createdDate', 'updatedDate')


class RevenueConfigSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = RevenueConfig
        fields = ('BeepToCallGap', 'isActive', 'createdDate', 'updatedDate')


class FreebiesSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = Freebies
        fields = ('id', 'Name', 'createdDate', 'updatedDate')


class FreebiesTypeSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    class Meta:
        model = FreebiesType
        fields = ('id', 'Name', 'createdDate', 'updatedDate')


