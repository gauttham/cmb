from .models import ExceptionList, DedicatedAccount, PrepaidInCdr, DaInCdrMap, ServiceClass
from django.db import connection
from . import constants


def RevenueCalculator():
    """
    Calculates the revenue for each row and updates the row with the generated revenue
    :return: True/False
    """
    for row in PrepaidInCdr.objects.all():
        pass


def customSql(sqlstr):
    cursor = connection.cursor()
    cursor.execute(str(sqlstr))
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]




