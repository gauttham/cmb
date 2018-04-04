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
    daId = serializers.CharField(source='dedicatedAccount')
    class Meta:
        model = DaInCdrMap
        fields = ('id', 'PrepaidInCdr', 'daId', 'valueBeforeCall', 'valueAfterCall',
                  'createdDate', 'updatedDate', 'createdBy', 'updatedBy')


class DaInCdrMapforInCDRSerializer(serializers.ModelSerializer):
    daId = serializers.CharField(source='dedicatedAccount')

    class Meta:
        model = DaInCdrMap
        fields = ('daId', 'valueBeforeCall', 'valueAfterCall')


class PrepaidInCdrSerializer(serializers.ModelSerializer):
    callStartTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    dedicatedAccounts = DaInCdrMapforInCDRSerializer(many=True)
    daCount = serializers.SerializerMethodField('get_das_count')

    class Meta:
        model = PrepaidInCdr
        fields = ('id', 'serviceClass', 'accountValueBeforeCall', 'accountValueAfterCall', 'callCharge',
                  'chargedDuration', 'callStartTime', 'callerNumber', 'calledNumber', 'redirectingNumber',
                  'gsmCallRefNumber', 'presentationIndicator', 'revenueShared', 'reason', 'dedicatedAccounts',
                  'daCount', 'createdDate', 'updatedDate', 'createdBy', 'updatedBy')

    def get_das_count(self, obj):
        return obj.dedicatedAccounts.count()

    def create(self, validated_data):
        das_data = validated_data.pop('dedicatedAccounts')
        validated_data['serviceClass']
        inCdr = PrepaidInCdr.objects.create(**validated_data)
        for da_data in das_data:
            DaInCdrMap.objects.create(PrepaidInCdr=inCdr, **da_data)
        return {'status': 'Success'}

    def update(self, instance, validated_data):
        das_data = validated_data.pop('dedicatedAccounts')
        das = instance.dedicatedAccounts.all()
        das = list(das)
        instance.serviceClass = validated_data.get('serviceClass', instance.serviceClass)
        instance.accountValueBeforeCall = validated_data.get('accountValueBeforeCall', instance.accountValueBeforeCall)
        instance.accountValueAfterCall = validated_data.get('accountValueAfterCall', instance.accountValueAfterCall)
        instance.callCharge = validated_data.get('callCharge', instance.callCharge)
        instance.chargedDuration = validated_data.get('chargedDuration', instance.chargedDuration)
        instance.callStartTime = validated_data.get('callStartTime', instance.callStartTime)
        instance.callerNumber = validated_data.get('callerNumber', instance.callerNumber)
        instance.calledNumber = validated_data.get('calledNumber', instance.calledNumber)
        instance.redirectingNumber = validated_data.get('redirectingNumber', instance.redirectingNumber)
        instance.gsmCallRefNumber = validated_data.get('gsmCallRefNumber', instance.gsmCallRefNumber)
        instance.presentationIndicator = validated_data.get('presentationIndicator', instance.presentationIndicator)
        instance.revenueShared = validated_data.get('revenueShared', instance.revenueShared)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.save()

        for da_data in das_data:
            da = das.pop(0)
            da.PrepaidInCdr = PrepaidInCdr.objects.get(pk=instance.pk)
            da.valueBeforeCall = da_data.get('valueBeforeCall', da.valueBeforeCall)
            da.save()

        return {'status': 'Success'}


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


