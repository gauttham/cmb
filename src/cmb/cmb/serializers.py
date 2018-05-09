from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, ServiceClass, DedicatedAccount, ExceptionList, InCdr, DaInCdrMap, \
    Roles, beepCDR, RevenueConfig, Freebies, FreebiesType, BulkLoadHistory, BulkLoadFailedList
from django.utils import timezone
from . import constants
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class ServiceClassSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    def create(self, validated_data):
        try:
            ServiceClass.objects.create(**validated_data)
            return {'status': '1'}
        except Exception as e:
            print ("Some Error Occurred")
            return {'status': '0'}

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.description = validated_data.get('description', instance.description)
        instance.isRevenueShare = validated_data.get('isRevenueShare', instance.isRevenueShare)
        instance.inMobilesPercentage = validated_data.get('inMobilesPercentage', instance.inMobilesPercentage)
        instance.updatedDate = timezone.now
        instance.otherOperatorPercentage = validated_data.get('otherOperatorPercentage', instance.otherOperatorPercentage)
        instance.save()
        return {'status': '1'}

    class Meta:
        model = ServiceClass
        fields = ('id', 'description', 'isRevenueShare', 'inMobilesPercentage',
                  'otherOperatorPercentage', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class DedicatedAccountSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    def create(self, validated_data):
        try:
            DedicatedAccount.objects.create(**validated_data)
            return {'status': '1'}
        except Exception as e:
            print ("Some Error Occurred")
            return {'status': '0'}

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.product = validated_data.get('product', instance.product)
        instance.type = validated_data.get('type', instance.type)
        instance.sub_type = validated_data.get('sub_type', instance.sub_type)
        instance.updatedDate = timezone.now
        instance.updatedBy = validated_data.get('updatedBy', instance.updatedBy)
        instance.save()
        return {'status': '1'}

    class Meta:
        model = DedicatedAccount
        fields = ('id', 'product', 'type', 'sub_type', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class ExceptionListSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)

    def create(self, validated_data):
        try:
            ExceptionList.objects.create(**validated_data)
            return {'status': '1'}
        except Exception as e:
            print ("Some Error Occurred")
            return {'status': '0'}

    def update(self, instance, validated_data):
        instance.msisdn = validated_data.get('msisdn', instance.msisdn)
        instance.msisdnType = validated_data.get('msisdnType', instance.msisdnType)
        instance.updatedDate = timezone.now
        instance.updatedBy = validated_data.get('updatedBy', instance.updatedBy)
        instance.save()
        return {'status': '1'}

    class Meta:
        model = ExceptionList
        fields = ('msisdn', 'msisdnType', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class DaInCdrMapSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    daId = serializers.CharField(source='dedicatedAccount')

    def create(self, validated_data):
        try:
            DaInCdrMap.objects.create(**validated_data)
            return {'status': '1'}
        except Exception as e:
            print ("Some Error Occurred")
            return {'status': '0'}

    def update(self, instance, validated_data):
        instance.InCdr = validated_data.get('InCdr', instance.InCdr)
        instance.dedicatedAccount = validated_data.get('dedicatedAccount', instance.dedicatedAccount)
        instance.valueBeforeCall = validated_data.get('valueBeforeCall', instance.valueBeforeCall)
        instance.valueAfterCall = validated_data.get('valueAfterCall', instance.valueAfterCall)
        instance.updatedDate = timezone.now
        instance.updatedBy = validated_data.get('updatedBy', instance.updatedBy)
        instance.save()
        return {'status': '1'}

    class Meta:
        model = DaInCdrMap
        fields = ('id', 'PrepaidInCdr', 'daId', 'valueBeforeCall', 'valueAfterCall',
                  'createdDate', 'updatedDate', 'createdBy', 'updatedBy')


class DaInCdrMapforInCDRSerializer(serializers.ModelSerializer):
    daId = serializers.CharField(source='dedicatedAccount')

    def create(self, validated_data):
        try:
            DaInCdrMap.objects.create(**validated_data)
            return {'status': '1'}
        except Exception as e:
            print ("Some Error Occurred")
            return {'status': '0'}

    def update(self, instance, validated_data):
        instance.InCdr = validated_data.get('InCdr', instance.InCdr)
        instance.dedicatedAccount = validated_data.get('dedicatedAccount', instance.dedicatedAccount)
        instance.valueBeforeCall = validated_data.get('valueBeforeCall', instance.valueBeforeCall)
        instance.valueAfterCall = validated_data.get('valueAfterCall', instance.valueAfterCall)
        instance.updatedDate = timezone.now
        instance.updatedBy = validated_data.get('updatedBy', instance.updatedBy)
        instance.save()
        return {'status': '1'}



    class Meta:
        model = DaInCdrMap
        fields = ('daId', 'valueBeforeCall', 'valueAfterCall')


class InCdrSerializer(serializers.ModelSerializer):
    callStartTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    updatedDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default=timezone.now)
    dedicatedAccounts = DaInCdrMapforInCDRSerializer(many=True)
    daCount = serializers.SerializerMethodField('get_das_count')

    class Meta:
        model = InCdr
        fields = ('id', 'serviceClass', 'accountValueBeforeCall', 'accountValueAfterCall', 'callCharge',
                  'chargedDuration', 'callStartTime', 'callerNumber', 'calledNumber', 'subscriberType', 'redirectingNumber',
                  'gsmCallRefNumber', 'presentationIndicator', 'revenueShared', 'reason', 'dedicatedAccounts',
                  'daCount', 'createdDate', 'updatedDate', 'createdBy', 'updatedBy')

    def get_das_count(self, obj):
        return constants.daCount
        # return obj.dedicatedAccounts.count()

    def create(self, validated_data):
        das_data = validated_data.pop('dedicatedAccounts')
        validated_data['serviceClass']
        inCdr = InCdr.objects.create(**validated_data)
        for da_data in das_data:
            DaInCdrMap.objects.create(InCdr=inCdr, **da_data)
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
        instance.subscriberType = validated_data.get('subscriberType', instance.subscriberType)
        instance.redirectingNumber = validated_data.get('redirectingNumber', instance.redirectingNumber)
        instance.gsmCallRefNumber = validated_data.get('gsmCallRefNumber', instance.gsmCallRefNumber)
        instance.presentationIndicator = validated_data.get('presentationIndicator', instance.presentationIndicator)
        instance.revenueShared = validated_data.get('revenueShared', instance.revenueShared)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.save()

        for da_data in das_data:
            da = das.pop(0)
            da.InCdr = InCdr.objects.get(pk=instance.pk)
            da.valueBeforeCall = da_data.get('valueBeforeCall', da.valueBeforeCall)
            da.save()

        return {'status': '1'}


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


class BulkHistorySerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BulkLoadHistory
        fields = ('id', 'type', 'initialCount', 'status', 'errorCount', 'start', 'end', 'uploadedBy')


class BulkLoadFailedSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BulkLoadFailedList
        fields = ('id', 'BulkLoadHistory', 'cdr', 'error', 'createdDate', 'uploadedBy')

#
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#     def create(self, validated_data):
#         user = super(UserSerializer, self).get_or_create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('roleName', 'createdBy')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserListSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateTimeField(source='date_joined', format="%Y-%m-%d %H:%M:%S")
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    lastLogin = serializers.DateTimeField(source='last_login', format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'lastLogin', 'createdDate')


