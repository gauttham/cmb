from .models import  ServiceClass, DedicatedAccount, ExceptionList, PrepaidInCdr, DaInCdrMap, beepCDR, RevenueConfig, Freebies, FreebiesType
from .serializers import ServiceClassSerializer, DedicatedAccountSerializer, ExceptionListSerializer, DaInCdrMapSerializer, PrepaidInCdrSerializer, beepCDRSerializer, RevenueConfigSerializer, FreebiesSerializer, FreebiesTypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .controllers import RevenueCalculator, generateReport1, generateRevenueReport, generateNonRevenueReport
from datetime import datetime
from . import loader
from .decorators import loadCsv

# Imports for Authentication
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken .models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login Failed"}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"status":"0", "description": "Login Failed"})


def dec(func):
    def wrapper(*args, **kwargs):
        print("Something is happening ")
        print(args[0], args[1].query_params.get('format'))
        return func(*args, **kwargs)

    return wrapper


class ServiceClassList(APIView):
    """
    List all Service Classes, or create a new service class
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = ServiceClass.objects.all()
        serializer = ServiceClassSerializer(dataset, many=True)
        # return Response(serializer.data)
        return serializer

    def post(self, request, format=None):
        serializer = ServiceClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class ServiceClassDetails(APIView):
    """

    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


#######
class DedicatedAccountList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = DedicatedAccount.objects.all()
        serializer = DedicatedAccountSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = DedicatedAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class DedicatedAccountDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})

#####

class ExceptionListList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = ExceptionList.objects.all()
        serializer = ExceptionListSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = ExceptionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('msisdn')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class ExceptionListDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


######

class PrepaidInCdrList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        RevenueCalculator()
        dataset = PrepaidInCdr.objects.all()
        serializer = PrepaidInCdrSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        # Handling the date format from the file
        callStartTime = request.data.get('callStartTime')
        request.data['callStartTime'] = datetime.strptime(callStartTime, '%d/%m/%y %H:%M:%S').strftime(
            '%Y-%m-%d %H:%M:%S')
        serializer = PrepaidInCdrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class PrepaidInCdrDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


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
        callStartTime = request.data.get('callStartTime')
        request.data['callStartTime'] = datetime.strptime(callStartTime, '%d/%m/%y %H:%M:%S').strftime(
            '%Y-%m-%d %H:%M:%S')
        serializer = PrepaidInCdrSerializer(dataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


######
class DaInCdrMapList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    @loadCsv
    def get(self, request, format=None):
        dataset = DaInCdrMap.objects.all()
        serializer = DaInCdrMapSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = DaInCdrMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class DaInCdrMapDetails(APIView):
    """

    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})

########

class BeepCDRList(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = beepCDR.objects.all()
        serializer = beepCDRSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = beepCDRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class BeepCDRDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


#######

class RevenueConfigList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = RevenueConfig.objects.all()
        serializer = RevenueConfigSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = RevenueConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class RevenueConfigDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


####

class FreebiesList(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = Freebies.objects.all()
        serializer = FreebiesSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = FreebiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class FreebiesDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


###

class FreebiesTypeList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @loadCsv
    def get(self, request, format=None):
        dataset = FreebiesType.objects.all()
        serializer = FreebiesTypeSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = FreebiesTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class FreebiesTypeDetails(APIView):
    """

    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


class BulkLoader(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        userName = request.GET.get('userName')
        tableName = request.GET.get('tableName')
        filePath = request.GET.get('filePath')

        if tableName == 'dedicatedAccount':
            try:
                loader.loadDedicatedAccount(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'exceptionList':
            try:
                loader.loadExceptionList(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'serviceClass':
            try:
                loader.loadServiceClass(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})
        elif tableName == 'PrepaidInCDR':
            try:
                result = loader.loadCdr(userName, filePath)
                return Response(result)
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        else:
            return {'status': '0',
                    'description': 'Wrong table name, please use serviceClass, dedicatedAccount, exceptionList'}

    def post(self, request):
        userName = request.data.get('userName')
        tableName = request.data.get('tableName')
        filePath = request.data.get('filePath')
        if tableName == 'dedicatedAccount':
            try:
                loader.loadDedicatedAccount(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'exceptionList':
            try:
                loader.loadExceptionList(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'serviceClass':
            try:
                loader.loadServiceClass(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'PrepaidInCDR':
            try:
                result = loader.loadCdr(userName, filePath)
                return Response(result)
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        else:
            return {'status': '0',
                    'description': 'Wrong table name, please use serviceClass, dedicatedAccount, exceptionList'}


class Report1(APIView):

    @loadCsv
    def get(self, request):
        result = generateReport1(request)
        return Response(result)


class RevenueReport(APIView):
    @loadCsv
    def get(self, request):
        result = generateRevenueReport(request)
        return Response(result)


class NoNRevenueReport(APIView):
    @loadCsv
    def get(self, request):
        result = generateNonRevenueReport(request)
        return Response(result)
