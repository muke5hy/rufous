from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from register.models import Register
from register.serializers import RegisterSerializer
from rest_framework import serializers, viewsets, routers


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

    def register_view( self,request):

        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)