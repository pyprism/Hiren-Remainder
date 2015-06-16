from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, ReminderSerializer
from .models import Reminder
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReminderViewSet(generics.DestroyAPIView, viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    paginate_by = 15
