from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from jobs.models import Jobs
from jobs.serializers import JobsSerializer
from rest_framework import serializers, viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404

class JobsList(APIView):
    

    def get(self, request, format=None):
        jobs = Jobs.objects.all()
        serializer = JobsSerializer(Jobs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobsDetail(APIView):
    """
    Retrieve, update or delete a Register instance.
    """
    def get_object(self, pk):
        try:
            return Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jobs = self.get_object(pk)
        serializer = JobsSerializer(jobs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jobs = self.get_object(pk)
        serializer = JobsSerializer(jobs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jobs = self.get_object(pk)
        jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
