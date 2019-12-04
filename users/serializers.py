from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','name','role']


class UserProfileerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['user','title','address','country','city','zip','photo']