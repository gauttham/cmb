import csv
from django.http import HttpResponse
from rest_framework.response import Response


def loadCsv(func):

    def wrapper(*args, **kwargs):
        request = args[1]
        if request.GET.get('csv') == 'true':
            header = []
            resultserializer = func(*args, **kwargs)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="BulkExport.csv"'
            # header = resultserializer.Meta.fields
            print(resultserializer.data[0])
            for item in resultserializer.data[0].iterkeys():
                header.append(item)
            writer = csv.DictWriter(response, fieldnames=header)
            for row in resultserializer.data:
                print(row)
                writer.writerow(row)
            return response

        else:
            resultserializer = func(*args, **kwargs)
            return Response(resultserializer.data)

    return wrapper


