from rest_framework import serializers
from .models import Users, UsersProfile


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username','first_name','last_name','email','role']


class UsersProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersProfile
        fields = ['user','title','address','country','city','zip','photo']