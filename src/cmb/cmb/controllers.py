from .models import ExceptionList, DedicatedAccount, InCdr, DaInCdrMap, ServiceClass, RevenueConfig
from django.db import connection
from . import constants
from .constants import RevenueCalculatorQuery, postpaidRevenueQuery, updateReasonMoreThan1HourPostpaid, updateReasonMoreThan1HourPrepaid
from datetime import datetime, timedelta
from . import serializers as cmbserializers


def getRevenueConfig(category):
    try:
        revenueConfig = RevenueConfig.objects.get(category=category, isActive=True)
        return revenueConfig
    except Exception as e:
        return str(e)


def getRevenueMetadatafromSC(row):
    serviceClass = ServiceClass.objects.get(id=row.get('serviceClass_id'))
    return serviceClass


def isServiceClassValid(row):
    flag = ServiceClass.objects.get(id=row.get('serviceClass_id'))
    return flag.isRevenueShare


def RevenueCalculatorPrepaid():
    """
    Calculates the revenue for each row and updates the row with the generated revenue
    :return: True/False
    """
    # Revenue Config will be used to parameterize the Revenue Calculator Query
    revenueConfig = getRevenueConfig('Prepaid')
    queryStr = RevenueCalculatorQuery % (revenueConfig.BeepToCallGap, revenueConfig.timeDuration)

    try:
        # For prepaid revenue
        for row in executeCustomSql(queryStr):

            flag = isServiceClassValid(row)
            scMetadata = getRevenueMetadatafromSC(row)
            dataToSave = {}
            if flag == False:
                m = InCdr.objects.get(id=row.get('id'))
                m.revenueShared = 0
                m.reason = 'Wrong SC'
                m.createdDate = datetime.now()
                m.updatedDate = datetime.now()
                try:
                    m.save()
                except Exception as e:
                    print(str(e))
                continue
            else:
                for da in DaInCdrMap.objects.filter(InCdr=row.get('id')):
                    if da.valueBeforeCall > da.valueAfterCall:
                        m = InCdr.objects.get(id=row.get('id'))
                        if m.presentationIndicator == 1:
                            # handling the case for private flag
                            m.revenueShared = (row.get('callCharge') - scMetadata.privateFlagCost) * scMetadata.inMobilesPercentage / 100
                            m.MICRevenue = (row.get('callCharge') - scMetadata.privateFlagCost) * scMetadata.otherOperatorPercentage / 100
                        else:
                            m.revenueShared = row.get('callCharge')  * scMetadata.inMobilesPercentage / 100
                            m.MICRevenue = row.get('callCharge')  * scMetadata.otherOperatorPercentage / 100
                        m.createdDate = datetime.now()
                        m.updatedDate = datetime.now()
                        try:
                            m.save()
                        except Exception as e:
                            print(str(e))
                    else:
                        m = InCdr.objects.get(id=row.get('id'))
                        m.revenueShared = 0
                        m.reason = 'Wrong DA'
                        m.createdDate = datetime.now()
                        m.updatedDate = datetime.now()
                        try:
                            m.save()
                        except Exception as e:
                            print(str(e))
    except Exception as e:
        print ("Some Error Occurred:", str(e))

def RevenueCalculatorPostpaid():
    """
    Calculates the revenue for each row and updates the row with the generated revenue
    :return: True/False
    """
    # Revenue Config will be used to parameterize the Revenue Calculator Query
    revenueConfig = getRevenueConfig('Postpaid')
    postpaidQueryStr = postpaidRevenueQuery % (revenueConfig.BeepToCallGap, revenueConfig.timeDuration)
    print (postpaidQueryStr)
    try:
        for row in executeCustomSql(postpaidQueryStr):
            m = InCdr.objects.get(id=row.get("id"))
            m.revenueShared = row.get('callCharge') / 2
            m.MICRevenue = row.get('callCharge') / 2
            m.dedicatedAccounts = []
            try:
                m.save()
            except Exception as e:
                print("Some Error Occurred While Saving:", str(e))
    except Exception as e:
        print("Some Error Occurred", e)
        return False

        # 
def executeCustomSql(sqlstr):
    cursor = connection.cursor()
    cursor.execute(str(sqlstr))
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]


def generateReport1(start, end):

    queryStr = constants.report1 % (start, end)
    try:
        data = executeCustomSql(queryStr)
        return data
    except Exception as e:
        print("Some Error Occurred:", e)


def generateRevenueReport(start, end, aggregation):
    if aggregation == 'Hourly':
        aggstr = '%Y-%m-%d %H'
    elif aggregation == 'Daily':
        aggstr = '%Y-%m-%d'
    elif aggregation == 'Monthly':
        aggstr = '%Y-%m'
    else:
        aggstr = '%Y'
    queryStr = constants.revenueReport % ( aggstr, start, end, aggstr)
    try:
        data = executeCustomSql(queryStr)
        return data
    except Exception as e:
        print("Some Error Occurred:", e)


def generateNonRevenueReport(start, end):

    queryStr = constants.nonRevenueReport % (start, end)
    try:
        data = executeCustomSql(queryStr)
        return data
    except Exception as e:
        print("Some Error Occurred:", e)


def generateStats1(start, end):
    queryStr1 = constants.beep_info % (start, end)
    queryStr2 = constants.cdrinfo % (start, end)
    try:
        data1 = executeCustomSql(queryStr1)
        data2 = executeCustomSql(queryStr2)
        data1[0].update(data2[0])

        return data1
    except Exception as e:
        print("Some Error Occurred")


def updatedMissedRecordsPrepaid():
    try:
        data1 = executeCustomSql(updateReasonMoreThan1HourPrepaid)
        return True
    except Exception as e:
        print("Some Error Occurred", str(e))


def updatedMissedRecordsPostpaid():
    try:
        data1 = executeCustomSql(updateReasonMoreThan1HourPostpaid)
        return True
    except Exception as e:
        print("Some Error Occurred")