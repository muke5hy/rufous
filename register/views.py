from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from register.models import Register
from register.serializers import RegisterSerializer
from rest_framework import serializers, viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404

class RegisterList(APIView):
    """
    List all Registers, or create a new Register.
    """
    def get(self, request, format=None):
        Registers = Register.objects.all()
        serializer = RegisterSerializer(Registers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterDetail(APIView):
    """
    Retrieve, update or delete a Register instance.
    """
    def get_object(self, pk):
        try:
            return Register.objects.get(pk=pk)
        except Register.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        register = self.get_object(pk)
        serializer = RegisterSerializer(register)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        register = self.get_object(pk)
        serializer = RegisterSerializer(register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)