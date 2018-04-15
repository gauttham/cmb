from .models import ExceptionList, DedicatedAccount, PrepaidInCdr, DaInCdrMap, ServiceClass, RevenueConfig
from django.db import connection
from . import constants
from .constants import RevenueCalculatorQuery
from datetime import datetime, timedelta
from . import serializers as cmbserializers


def getRevenueConfig():
    revenueConfig = RevenueConfig.objects.get(isActive=1)
    return revenueConfig


def getRevenueMetadatafromSC(row):
    serviceClass = ServiceClass.objects.get(id=row.get('serviceClass_id'))
    return serviceClass


def isServiceClassValid(row):
    flag = ServiceClass.objects.get(id=row.get('serviceClass_id'))
    return flag.isRevenueShare


def RevenueCalculator():
    """
    Calculates the revenue for each row and updates the row with the generated revenue
    :return: True/False
    """

    # Revenue Config will be used to parameterize the Revenue Calculator Query
    revenueConfig = getRevenueConfig()
    queryStr = RevenueCalculatorQuery % (revenueConfig.BeepToCallGap, revenueConfig.timeDuration)
    try:
        for row in executeCustomSql(queryStr):

            flag = isServiceClassValid(row)
            scMetadata = getRevenueMetadatafromSC(row)

            if flag == False:
                row.revenueShared = 0
                row.reason = 'Wrong SC'
                serializer = cmbserializers.PrepaidInCdrSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()
                continue
            else:
                for da in DaInCdrMap.objects.filter(PrepaidInCdr=row.get('CDRID')):
                    if da.valueBeforeCall > da.valueAfterCall:
                        row['revenueShared'] = row.get('callCharge') * scMetadata.inMobilesPercentage / 100
                        row['MICRevenue'] = row.get('callCharge') * scMetadata.otherOperatorPercentage / 100
                        serializer = cmbserializers.PrepaidInCdrSerializer(data=row)
                        if serializer.is_valid():
                            serializer.save()
                        continue
                    else:
                        row['revenueShared'] = 0
                        row['reason'] = 'Wrong DA'
                        serializer = cmbserializers.PrepaidInCdrSerializer(data=row)
                        if serializer.is_valid():
                            serializer.save()
    except Exception as e:
        print ("Some Error Occurred:", str(e))


def executeCustomSql(sqlstr):
    cursor = connection.cursor()
    cursor.execute(str(sqlstr))
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]


def generateReport1(request):
    start = str(request.query_params.get('start'))
    end = str(request.query_params.get('end'))
    queryStr = constants.report1 % (start, end)
    try:
        data = executeCustomSql(queryStr)
        return data
    except Exception as e:
        print("Some Error Occurred:", e)


def generateRevenueReport(request):
    start = str(request.query_params.get('start'))
    end = str(request.query_params.get('end'))
    queryStr = constants.revenueReport % (start, end)
    try:
        data = executeCustomSql(queryStr)
        return data
    except Exception as e:
        print("Some Error Occurred:", e)


def generateNonRevenueReport(request):
    start = str(request.query_params.get('start'))
    end = str(request.query_params.get('end'))
    queryStr = constants.nonRevenueReport % (start, end)
    try:
        data = executeCustomSql(queryStr)
        return data
    except Exception as e:
        print("Some Error Occurred:", e)

