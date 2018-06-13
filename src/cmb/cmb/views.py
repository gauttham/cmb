from .models import ServiceClass, DedicatedAccount, ExceptionList, InCdr, DaInCdrMap, beepCDR, RevenueConfig, Freebies, \
    FreebiesType, BulkLoadHistory, BulkLoadFailedList, userRoles, Roles, revenueCalculation
from .serializers import ServiceClassSerializer, DedicatedAccountSerializer, ExceptionListSerializer, \
    DaInCdrMapSerializer, InCdrSerializer, beepCDRSerializer, RevenueConfigSerializer, FreebiesSerializer, \
    FreebiesTypeSerializer, BulkHistorySerializer, BulkLoadFailedSerializer, UserSerializer, RoleSerializer, \
    UserListSerializer, revenueCalculationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .controllers import generateReport1, generateRevenueReport, generateNonRevenueReport, \
    generateStats1
from datetime import datetime
from . import loader
import json
from .decorators import loadCsv
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.decorators import api_view, permission_classes
from . import tasks
import pandas as pd


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

class InCdrList(APIView):

    @loadCsv
    def get(self, request, format=None):
        # RevenueCalculator()
        dataset = InCdr.objects.all()
        serializer = InCdrSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        # Handling the date format from the file
        callStartTime = request.data.get('callStartTime')
        request.data['callStartTime'] = datetime.strptime(callStartTime, '%d/%m/%y %H:%M:%S').strftime(
            '%Y-%m-%d %H:%M:%S')
        serializer = InCdrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class InCdrDetails(APIView):
    """

    """


    def get_object(self, id):
        try:
            return InCdr.objects.get(pk=id)
        except ServiceClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = InCdrSerializer(dataset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataset = self.get_object(pk)
        callStartTime = request.data.get('callStartTime')
        request.data['callStartTime'] = datetime.strptime(callStartTime, '%d/%m/%y %H:%M:%S').strftime(
            '%Y-%m-%d %H:%M:%S')
        serializer = InCdrSerializer(dataset, data=request.data)
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

    @loadCsv
    def get(self, request, format=None):
        dataset = RevenueConfig.objects.all()
        serializer = RevenueConfigSerializer(dataset, many=True)
        return serializer

    def post(self, request, format=None):
        serializer = RevenueConfigSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get("isActive") == True:
                try:
                    m = RevenueConfig.objects.get(isActive=True, category=request.data.get("category"))
                    m.isActive = False
                    m.save()
                except Exception as e:
                    print(str(e))
                    pass
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


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
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('id')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response({'status': '1'})


####

class FreebiesList(APIView):

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

    def get(self, request):
        userName = request.query_params.get('userName')
        tableName = request.query_params.get('tableName')
        filePath = request.query_params.get('filePath')

        try:
            validateFile = pd.read_csv(filePath, nrows=2)
        except Exception as e:
            return Response({"status": "0", "description": str(e)})


        if tableName == 'dedicatedAccount':
            try:
                tasks.BulkloadDedicatedAccount.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'exceptionList':
            try:
                tasks.BulkLoadExceptionList.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'serviceClass':
            try:
                tasks.BulkloadServiceClass.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})
        elif tableName == 'PrepaidInCDR':
            try:
                tasks.BulkLoadPrepaidInCDR.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        elif tableName == 'postCdr':
            try:
                tasks.BulkLoadPostCDR.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        elif tableName == 'beepCdr':
            try:
                tasks.BulkLoadBeepCDR.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        else:
            return Response({'status': '0',
                             'description': 'Wrong table name, please use serviceClass, dedicatedAccount, '
                                            'exceptionList, PrepaidInCDR, beepCdr, postCdr'})

    def post(self, request):
        userName = request.data.get('userName')
        tableName = request.data.get('tableName')
        filePath = request.data.get('filePath')

        try:
            validateFile = pd.read_csv(filePath, nrows=2)
        except Exception as e:
            return Response({"status": "0", "description": str(e)})

        if tableName == 'dedicatedAccount':
            try:
                tasks.BulkloadDedicatedAccount.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'exceptionList':
            try:
                tasks.BulkLoadExceptionList.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'serviceClass':
            try:
                tasks.BulkloadServiceClass.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                print("Some Error Occurred: ", e)
                return Response({'status': '0', 'description': str(e)})

        elif tableName == 'PrepaidInCDR':
            try:
                tasks.BulkLoadPrepaidInCDR.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})

        elif tableName == 'postCdr':
            try:
                tasks.BulkLoadPostCDR.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        elif tableName == 'beepCdr':
            try:
                tasks.BulkLoadBeepCDR.delay(userName, filePath)
                return Response({'status': '1'})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        else:
            return Response({'status': '0',
                             'description': 'Wrong table name, please use serviceClass, dedicatedAccount, exceptionList'})


class Report1(APIView):

    @loadCsv
    def get(self, request):
        start = str(request.query_params.get('start'))
        end = str(request.query_params.get('end'))
        result = generateReport1(start, end)
        return Response(result)


class RevenueReport(APIView):

    @loadCsv
    def get(self, request):
        start = str(request.query_params.get('start'))
        end = str(request.query_params.get('end'))
        aggregation = str(request.query_params.get("timeType"))
        result = generateRevenueReport(start, end, aggregation)
        return Response(result)


class NoNRevenueReport(APIView):

    @loadCsv
    def get(self, request):
        start = str(request.query_params.get('start'))
        end = str(request.query_params.get('end'))
        result = generateNonRevenueReport(start, end)
        return Response(result)


class Stats1(APIView):

    @loadCsv
    def get(self, request):
        start = str(request.query_params.get('start'))
        end = str(request.query_params.get('end'))
        result = generateStats1(start, end)
        return Response(result)


class ExecuteRevenueCalculatorPrepaid(APIView):

    def get(self, request):
        try:
            tasks.RevenueCalculatorPrepaid.delay()
            # tasks.RevenueCalculatorPrepaid()
            print("Revenue calculator started for Prepaid...")
            return Response({"status": "1", "description": "Revenue calculation Started"})
        except Exception as e:
            return Response({"status": "0", "description": str(e)})


class ExecuteRevenueCalculatorPostpaid(APIView):

    def get(self, request):
        try:
            tasks.RevenueCalculatorPostpaid.delay()
            # tasks.RevenueCalculatorPostpaid()
            print("Revenue calculator started for Postpaid...")
            return Response({"status": "1", "description": "Revenue calculation Started"})
        except Exception as e:
            return Response({"status": "0", "description": str(e)})



class reports(APIView):

    @loadCsv
    def get(self, request):
        try:
            start = str(request.query_params.get('start'))
            end = str(request.query_params.get('end'))
            aggregation = str(request.query_params.get("timeType"))
            reportType = str(request.query_params.get("reportType"))

            if reportType == "revenueReport":
                result = generateRevenueReport(start, end, aggregation)
            elif reportType == "nonRevenueReport":
                result = generateNonRevenueReport(start, end)
            elif reportType == "stats1":
                result = generateStats1(start, end)
            elif reportType == "auditing1":
                result = generateReport1(start, end)
            else:
                result = {"status": "0", "description": "No Matching report type"}
            return Response(result)
        except Exception as e:
            return Response({"status": "0", "description": str(e)})


####


class BulkLoadHistoryList(APIView):

    @loadCsv
    def get(self, request, format=None):
        dataset = BulkLoadHistory.objects.all()
        serializer = BulkHistorySerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BulkHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('msisdn')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class BulkFailedList(APIView):

    @loadCsv
    def get(self, request, format=None):
        bulkLoadHistoryId = request.query_params.get("bulkLoadId")
        if bulkLoadHistoryId:
            BulkHistory = BulkLoadHistory.objects.get(pk=bulkLoadHistoryId)
            dataset = BulkLoadFailedList.objects.filter(BulkLoadHistory=BulkHistory)
        else:
            dataset = BulkLoadFailedList.objects.all().order_by('-id')[:10:1]
        serializer = BulkLoadFailedSerializer(dataset, many=True)
        return Response(serializer.data)


class login(APIView):
    def post(self, request, format='json'):
        username = request.data.get('username')
        password = request.data.get('password')
        authobj = BasicAuthentication()
        try:
            roleList = []
            res = authobj.authenticate_credentials(username, password)
            user = userRoles.objects.filter(user=User.objects.get(username=username))
            for indUser in user:
                for j in indUser.roles.all():
                    roleList.append(j.roleName)
            response = {"status": "1", "roles": roleList}
            return Response(response)
        except Exception as e:
            response = {"status": "0", "description": str(e)}
            return Response(response)


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class RoleList(APIView):

    def get(self, request):
        dataset = Roles.objects.all()
        serializer = RoleSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '1'})
        resp = {'status': '0', 'description': serializer.errors.get('msisdn')[0]}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):

    def get(self, request, format='json'):
        try:
            username = request.query_params.get('username')
            roleList = []
            user = userRoles.objects.filter(user=User.objects.get(username=username))
            for indUser in user:
                for j in indUser.roles.all():
                    roleList.append(j.roleName)
            response = {"status": "1", "roles": roleList}
            return Response(response)
        except Exception as e:
            response = {"status": "0", "description": str(e)}
            return Response(response)

    def post(self, request, format='json'):

        try:

            username = request.data.get('username')
            password = request.data.get('password')
            roles = request.data.get('roles')
            try:
                serializer = UserSerializer(data=request.data)
                try:
                    if serializer.is_valid():
                        serializer.save()

                    user = User.objects.create_user(username=username, password=password)
                except Exception as e:
                    user = User.objects.get(username=username)


                userRole = userRoles.objects.get_or_create(user=User.objects.get(username=username))
                # user = User.objects.get(username=username)

                # Remove the existing manytomany relationships
                try:
                    for i in userRole:
                        if not isinstance(i, bool):
                            for j in i.roles.all():
                                i.roles.remove(j)
                except Exception as e:
                    pass

                # Adding new roles passed to the User
                for role in roles:
                    try:
                        indRole = Roles.objects.get(roleName=role)
                        for i in userRole:
                            if not isinstance(i, bool):
                                i.roles.add(indRole)

                    except Exception as e:
                        return Response({"status": "0", "description": str(e)})
                return Response({"status": "1"})
            except Exception as e:
                return Response({"status": "0", "description": str(e)})
        except Exception as e:
            return Response({"status": "0", "description": str(e)})

    def delete(self, request, format='json'):
        try:
            user = User.objects.get(username=request.query_params.get('username'))
            user.delete()
            return Response({'status': '1'})
        except Exception as e:
            return Response(str(e))


class UserAdd(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):

    def get(self, request):
        try:
            username = request.query_params.get('username')
            if username:
                dataset = User.objects.filter(username=username)
            else:
                dataset = User.objects.all()
            serializer = UserListSerializer(dataset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e))


class revenueCalculationStatus(APIView):
    """
    List all Service Classes, or create a new service class
    """

    @loadCsv
    def get(self, request):
        dataset = revenueCalculation.objects.all()
        serializer = revenueCalculationSerializer(dataset, many=True)
        # return Response(serializer.data)
        return serializer