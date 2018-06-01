from __future__ import absolute_import, unicode_literals
import random
from celery.task import task, periodic_task
from .models import testModel
import requests
from datetime import timedelta, datetime
from .controllers import RevenueCalculatorPrepaid, RevenueCalculatorPostpaid
from . import loader
from . import controllers

@task(name="sum_two_numbers")
def add(x, y):
    print(x+y)
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


if __name__ == '__main__':
    @task(name="sum_list_numbers")
    def xsum(numbers):
        return sum(numbers)

# Scheduler task code starts from here.


# here we assume we want it to be run every 1 mins
# @periodic_task(run_every=datetime.timedelta(minutes=1))

@task(name="simple")
def myTask():
    return 'rec'


@task(name='insert_test')
def insertTest():
    m = testModel()
    m.name='gautam'
    m.save()
    return True


@task(name='generate_daily_stats1')
def generate_weekly_stats1():
    start = (datetime.now() - timedelta(days=7)).strftime(
                '%Y-%m-%d %H')
    end = datetime.now().strftime('%Y-%M-%d %H')
    reportType="Daily"
    url = "http://localhost:8000/reports/stats1/?start=%s&end=%s&reportType=%s" %(start, end, reportType)
    resp = requests.get(url)
    return resp



@task(name='RevenueCalculatorPrepaid')
def RevenueCalculatorPrepaid():
    controllers.RevenueCalculatorPrepaid()
    controllers.updatedMissedRecordsPrepaid()
    return True

@task(name='RevenueCalculatorPostpaid')
def RevenueCalculatorPostpaid():
    controllers.RevenueCalculatorPostpaid()
    controllers.updatedMissedRecordsPostpaid()
    return True

@task(name='BulkLoad-dedicatedAccount')
def BulkloadDedicatedAccount(userName, filePath):
    loader.loadDedicatedAccount(userName, filePath)


@task(name='BulkLoad-ExceptionList')
def BulkLoadExceptionList(userName, filePath):
    loader.loadExceptionList(userName, filePath)


@task(name='BulkLoad-serviceClass')
def BulkloadServiceClass(userName, filePath):
    loader.loadServiceClass(userName, filePath)


@task(name='BulkLoad-PrepaidInCDR')
def BulkLoadPrepaidInCDR(userName, filePath):
    loader.loadCdr(userName, filePath)


@task(name='BulkLoad-postCdr')
def BulkLoadPostCDR(userName, filePath):
    loader.loadPostCdr(userName, filePath)


@task(name='BulkLoad-beepCdr')
def BulkLoadBeepCDR(userName, filePath):
    loader.loadBeepCdr(userName, filePath)


@task(name="updatedMissedRecords")
def updatedMissedRecordsTask():
    controllers.updatedMissedRecords()

