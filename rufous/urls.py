"""rufous URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from register.views import RegisterList, RegisterDetail
from register.serializers import RegisterSerializer
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', schema_view),
    # path('register/', RegisterList.as_view()),
    # path('register/<int:pk>/', RegisterDetail.as_view()),
    path('users/', include('users.urls', namespace='users')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cities/', include('cities_light.contrib.restframework3')),
]