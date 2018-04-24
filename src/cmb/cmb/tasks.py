from __future__ import absolute_import, unicode_literals
import random
from celery.task import task, periodic_task
from .models import testModel
import requests
from datetime import timedelta, datetime
from .controllers import RevenueCalculator

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



@task(name='RevenueCalculator')
def RevenueCalculatorTask():
    RevenueCalculator()
    return True

