from rest_framework import serializers
from .models import Users, UsersProfile
from django.utils.translation import ugettext_lazy as _


class UsersSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255, required=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Users
        fields = ['username','first_name','last_name','email','role']


class UsersProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersProfile
        fields = ['user','title','address','country','city','zip','photo']