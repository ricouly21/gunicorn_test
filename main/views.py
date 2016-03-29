from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
