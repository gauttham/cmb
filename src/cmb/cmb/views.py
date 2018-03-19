from .models import Snippet, ServiceClass, DedicatedAccount, ExceptionList, PrepaidInCdr, DaInCdrMap
from .serializers import SnippetSerializer, ServiceClassSerializer, DedicatedAccountSerializer, ExceptionListSerializer, DaInCdrMapSerializer, PrepaidInCdrSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data)
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#####

class ExceptionListList(APIView):

    def get(self, request, format=None):
        dataset = ExceptionList.objects.all()
        serializer = DedicatedAccountSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExceptionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######

class PrepaidInCdrList(APIView):

    def get(self, request, format=None):
        dataset = PrepaidInCdr.objects.all()
        serializer = PrepaidInCdrSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrepaidInCdrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dataset = self.get_object(pk)
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

