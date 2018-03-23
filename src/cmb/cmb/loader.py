from .models import DedicatedAccount, ServiceClass, ExceptionList, PrepaidInCdr, DaInCdrMap, beepCDR
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


def loadDedicatedAccount(da):
    print("Now Loading Dedicated Account:")
    try:
        for row in da.iterrows():
            m = DedicatedAccount(id=row[1]['DA Id'])
            m.product = row[1]['Product/Plan']
            m.type = row[1]['Type']
            m.sub_type = row[1]['FREEBIES_TYPE']
            m.createdDate = datetime.now()
            m.updatedDate = datetime.now()
            m.save()
            return True
    except Exception as e:
        print("Some Error Occurred:", e)


def loadServiceClass(sc):
    try:
        for row in sc.iterrows():
            m = ServiceClass(id=row[1]['SC Id'])
            m.description = row[1]['SC DESCRIPTION']
            m.createdDate = datetime.now()
            m.updatedDate = datetime.now()
            m.save()
            return True
    except Exception as e:
        print("Some Error Occurred: ", e)


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

