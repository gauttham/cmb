from .models import ExceptionList, DedicatedAccount, PrepaidInCdr, DaInCdrMap, ServiceClass, RevenueConfig
from django.db import connection
from . import constants
from datetime import datetime, timedelta


def getRevenueConfig():
    revenueConfig = RevenueConfig.objects.get(isActive=True)
    return revenueConfig


def getRevenueMetadatafromSC(row):
    serviceClass = ServiceClass.objects.get(id=row.serviceClass_id)
    return serviceClass


def isServiceClassValid(row):
    flag = ServiceClass.objects.get(id = row.serviceClass_id)
    return flag.isRevenueShare


def RevenueCalculator():
    """
    Calculates the revenue for each row and updates the row with the generated revenue
    :return: True/False
    """
    revenueConfig = getRevenueConfig()

    for row in PrepaidInCdr.objects.filter(
            createdDate__gte=datetime.now() - timedelta(days=revenueConfig.timeDuration)):
        flag = isServiceClassValid(row)
        scMetadata = getRevenueMetadatafromSC(row)

        if flag == False:
            row.revenueShared = 0
            row.reason = 'Wrong SC'
            continue
        else:
            for da in DaInCdrMap.objects.filter(PrepaidInCdr=row.id):
                if da.valueBeforeCall > da.valueAfterCall:
                    row.revenueShared = row.callCharge * scMetadata.inMobilesPercentage / 100
                    row.save()
                    continue;
                else:
                    row.revenueShared = 0
                    row.reason = 'Wrong DA'
                    row.save()




def customSql(sqlstr):
    cursor = connection.cursor()
    cursor.execute(str(sqlstr))
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]




