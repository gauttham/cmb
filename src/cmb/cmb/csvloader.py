import csv

from rest_framework.views import APIView

from django.http import HttpResponse

from .serializers import DedicatedAccountSerializer

from .models import DedicatedAccount


class DAViewSet(APIView):
    serializer_class = DedicatedAccountSerializer

    def get_serializer(self, queryset, many=True):
        return self.serializer_class(
            queryset,
            many=True,
        )

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="BulkExport.csv"'
        serializer = self.get_serializer(DedicatedAccount.objects.all(), many=True)
        header = DedicatedAccountSerializer.Meta.fields
        print type(header)
        print(header)
        writer = csv.DictWriter(response, fieldnames=header)
        for row in serializer.data:
            writer.writerow(row)

        return response


