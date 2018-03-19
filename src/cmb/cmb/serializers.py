from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, ServiceClass, DedicatedAccount, ExceptionList, PrepaidInCdr, DaInCdrMap


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class ServiceClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceClass
        fields = ('id', 'description', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class DedicatedAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DedicatedAccount
        fields = ('id', 'product', 'type', 'sub_type', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class ExceptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionList
        fields = ('id', 'number', 'type', 'createdDate', 'updatedDate',
                  'createdBy', 'updatedBy')


class PrepaidInCdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrepaidInCdr
        fields = ('id', 'serviceClass', 'accountValueBeforeCall', 'accountValueAfterCall', 'callCharge',
                  'chargedDuration', 'callStartTime', 'callerNumber', 'calledNumber', 'redirectingNumber',
                  'GsmCallRefNumber', 'presentationIndicator', 'createdDate', 'updatedDate', 'createdBy', 'updatedBy')


class DaInCdrMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaInCdrMap
        fields = ('PrepaidInCdr', 'DedicatedAccount', 'valueBeforeCall', 'valueAfterCall',
                  'createdDate', 'updatedDate', 'createdBy', 'updatedBy')




