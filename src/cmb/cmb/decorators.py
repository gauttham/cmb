import csv
from django.http import HttpResponse
from rest_framework.response import Response
from collections import OrderedDict
from . import settings
from django.utils import timezone
from datetime import datetime


def loadCsv(func):

    def wrapper(*args, **kwargs):
        request = args[1]
        if request.query_params.get('csv'):
            header = []
            resultserializer = func(*args, **kwargs)
            response = HttpResponse(content_type='text/csv')
            if request.query_params.get("reportType") == "revenueReport":
                response['Content-Disposition'] = 'attachment; filename="RevenueReport-{timestamp}.csv"'\
                    .format(timestamp=datetime.now().strftime('%Y%m%d%H'))
            elif request.query_params.get("reportType") == "nonRevenueReport":
                response['Content-Disposition'] = 'attachment; filename="NonRevenueReport-{timestamp}.csv"'\
                    .format(timestamp=datetime.now().strftime('%Y%m%d%H'))
            elif request.query_params.get("reportType") == "stats1":
                response['Content-Disposition'] = 'attachment; filename="Stats1-{timestamp}.csv"'\
                    .format(timestamp=datetime.now().strftime('%Y%m%d%H'))
            elif request.query_params.get("reportType") == "auditing1":
                response['Content-Disposition'] = 'attachment; filename="Auditing1-{timestamp}.csv"'\
                    .format(timestamp=datetime.now().strftime('%Y%m%d%H'))
            else:
                response['Content-Disposition'] = 'attachment; filename="BulkExport-{timestamp}.csv"'\
                    .format(timestamp=datetime.now().strftime('%Y%m%d%H'))

            try:
                for item in resultserializer.data[0].iterkeys():
                    header.append(item)
                writer = csv.DictWriter(response, fieldnames=header)
                writer.writeheader()


                if request.query_params.get('reportType') == 'Generate':
                    pass
                else:
                    for row in resultserializer.data:
                        writer.writerow(row)

                    return response
            except Exception as e:
                writer = csv.DictWriter(response, fieldnames="Empty List")
                writer.writeheader()
                return response
                return Response("Empty Dataset")
                

        else:
            resultserializer = func(*args, **kwargs)
            return Response(resultserializer.data)

    return wrapper


