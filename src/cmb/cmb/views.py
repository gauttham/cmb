from .models import  ServiceClass, DedicatedAccount, ExceptionList, PrepaidInCdr, DaInCdrMap, beepCDR, RevenueConfig, Freebies, FreebiesType
from .serializers import ServiceClassSerializer, DedicatedAccountSerializer, ExceptionListSerializer, DaInCdrMapSerializer, PrepaidInCdrSerializer, beepCDRSerializer, RevenueConfigSerializer, FreebiesSerializer, FreebiesTypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .controllers import RevenueCalculator
from datetime import datetime


class ServiceClassList(APIView):
    """
    List all Service Classes, or create a new service class
    """
    def get(self, request, format=None):
        dataset = ServiceClass.objects.all()
        serializer = ServiceClassSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceClassDetails(APIView):
    """

    """
    def get_object(self, id):
        try:
            return ServiceClass.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = ServiceClassSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = ServiceClassSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#######
class DedicatedAccountList(APIView):

    def get(self, request, format=None):
        dataset = DedicatedAccount.objects.all()
        serializer = DedicatedAccountSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DedicatedAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DedicatedAccountDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return DedicatedAccount.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = DedicatedAccountSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = DedicatedAccountSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})

#####

class ExceptionListList(APIView):

    def get(self, request, format=None):
        dataset = ExceptionList.objects.all()
        serializer = ExceptionListSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExceptionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExceptionListDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return ExceptionList.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = ExceptionListSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = ExceptionListSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})


######

class PrepaidInCdrList(APIView):

    def get(self, request, format=None):
        RevenueCalculator()
        dataset = PrepaidInCdr.objects.all()
        serializer = PrepaidInCdrSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Handling the date format from the file
        callStartTime = request.data.get('callStartTime')
        request.data['callStartTime'] = datetime.strptime(callStartTime, '%d/%m/%y %H:%M:%S').strftime(
            '%Y-%m-%d %H:%M:%S')
        serializer = PrepaidInCdrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrepaidInCdrDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return PrepaidInCdr.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = PrepaidInCdrSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = PrepaidInCdrSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})


######
class DaInCdrMapList(APIView):

    def get(self, request, format=None):
        dataset = DaInCdrMap.objects.all()
        serializer = DaInCdrMapSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DaInCdrMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DaInCdrMapDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return DaInCdrMap.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = DaInCdrMapSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = DaInCdrMapSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})

########

class BeepCDRList(APIView):

    def get(self, request, format=None):
        dataset = beepCDR.objects.all()
        serializer = beepCDRSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = beepCDRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BeepCDRDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return beepCDR.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = beepCDRSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = beepCDRSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})


#######

class RevenueConfigList(APIView):

    def get(self, request, format=None):
        dataset = RevenueConfig.objects.all()
        serializer = RevenueConfigSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RevenueConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RevenueConfigDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return RevenueConfig.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = RevenueConfigSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = RevenueConfigSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})


####

class FreebiesList(APIView):

    def get(self, request, format=None):
        dataset = Freebies.objects.all()
        serializer = FreebiesSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FreebiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FreebiesDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return Freebies.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = FreebiesSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = FreebiesSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})


###

class FreebiesTypeList(APIView):

    def get(self, request, format=None):
        dataset = FreebiesType.objects.all()
        serializer = FreebiesTypeSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FreebiesTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FreebiesTypeDetails(APIView):
    """

    """

    def get_object(self, id):
        try:
            return FreebiesType.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = FreebiesTypeSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = FreebiesTypeSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': '1'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'Status': '1'})

