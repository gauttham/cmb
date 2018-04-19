from __future__ import absolute_import, unicode_literals
import random
from celery.task import task, periodic_task
import datetime
from .models import testModel


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




