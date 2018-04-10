from .models import DedicatedAccount, Freebies, ServiceClass, ExceptionList, PrepaidInCdr, DaInCdrMap, beepCDR, msisdnType
import pandas as pd
from datetime import datetime
from django.utils import timezone


def ReadInitialData():
    try:
        ppincdr = pd.read_excel('cmb/data/Dummy_Data.xlsx', 'Prepaid_IN_CDRS')
        beep_cdr = pd.read_excel('cmb/data/Dummy_Data.xlsx', 'Beep_CDRS')
        da = pd.read_excel('cmb/data/SC&DA.xlsx', 'DAs')
        sc = pd.read_excel('cmb/data/SC&DA.xlsx', 'SCs')
        return ppincdr, beep_cdr, da, sc
    except Exception as e:
        print ("Some Error Occurred: ", str(e))

def loadInitialData():
    try:
        ppincdr, beep_cdr, da, sc = ReadInitialData()

    except Exception as e:
        print("Some Error Occurred:", e)


def loadPrepaidInCrd(ppincdr):
    try:
        for row in ppincdr.iterrows():
            m = PrepaidInCdr(id=row[1]['Datastructure'])
            try:
                serviceClass = ServiceClass.objects.get(id=row[1]['serviceClass'])
            except ServiceClass.DoesNotExist:
                serviceClass = None
            m.serviceClass = serviceClass
            m.accountValueBeforeCall = row[1]['accountValueBeforeCall']
            m.accountValueAfterCall = row[1]['accountValueAfterCall']
            m.callCharge = row[1]['finalChargeofCall']
            m.chargedDuration = row[1]['chargedDuration']
            m.callStartTime = row[1]['timeandTimezoneforStartofCharging']
            m.callerNumber = row[1]['callingPartyNumber']
            m.calledNumber = row[1]['calledPartyNumber']
            m.redirectingNumber = row[1]['redirectingNumber'] if pd.isnull(row[1]['redirectingNumber']) else None
            m.GsmCallRefNumber = row[1]['gSMCallReferenceNumber']
            m.presentationIndicator = row[1]['presentationIndicator  ']
            m.createdDate = timezone.now()
            m.updatedDate = timezone.now()
            try:
                m.save()
            except ValueError as e:
                print(e)
                print(row)
    except Exception as e:
        print("Some Error Occurred:", e)


def loadBeepCDR(beep_cdr):
    try:
        for row in beep_cdr.iterrows():
            m = beepCDR(calledNumber=row[1]['calledPartyNumber'], callerNumber=row[1]['callingPartyNumber'],
                        callStartTime=row[1]['Add Time'], createdDate=timezone.now(), updatedDate=timezone.now())
            try:
                m.save()
            except Exception as e:
                print("Some Error Occurred:", e)
    except Exception as e:
        print("Some Error Occurred:", e)

# Bulk Loader Modules

def loadExceptionList(userName, filePath):

    try:
        exc = pd.read_csv(filePath)
        for row in exc.iterrows():
            m = ExceptionList(msisdn=str(row[1]['msisdn']))
            m.msisdnType = msisdnType.objects.get(id=row[1]['msisdnType'])
            m.createdBy = str(userName)
            m.updatedBy = str(userName)
            try:
                m.save()
            except Exception as e:
                print("Some Error Occurred while saving: ", str(e))
                print(row)
        return True
    except Exception as e:
        print("Some Error Occurred:", e)


def loadDedicatedAccount(userName, filePath):
    try:
        da = pd.read_csv(filePath)

        for row in da.iterrows():
            m = DedicatedAccount(id=row[1]['id'])
            m.product = row[1]['product']
            m.type = Freebies.objects.get(id=row[1]['type'])
            m.sub_type = str(row[1]['sub_type'])
            m.createdBy = userName
            m.updatedBy = userName
            try:
                m.save()
            except Exception as e:
                print("Some Error Occurred while saving: ", str(e))
                print(row)
        return True
    except Exception as e:
        print("Some Error Occurred: ", e)
        return False


def loadServiceClass(userName, filePath):
    try:
        sc = pd.read_csv(filePath)

        for row in sc.iterrows():
            m = ServiceClass(id=row[1]['id'])
            m.description = row[1]['description']
            m.isRevenueShare = row[1]['isRevenueShare']
            m.inMobilesPercentage = str(row[1]['inMobilesPercentage'])
            m.otherOperatorPercentage = str(row[1]['otherOperatorPercentage'])
            m.createdBy = userName
            m.updatedBy = userName
            try:
                m.save()
            except Exception as e:
                print("Some Error Occurred while saving: ", str(e))
                print(row)
        return True
    except Exception as e:
        print("Some Error Occurred: ", e)
        return False

