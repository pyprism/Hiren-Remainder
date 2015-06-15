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


class ReminderAll(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    paginate_by = 15


class Reminder(APIView):

    def get_object(self, pk):
        try:
            return Reminder.objects.get(pk=pk)
        except Reminder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reminder = self.get_object(pk)
        serializer_class = ReminderSerializer(reminder)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        reminder = self.get_object(pk)
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Test(viewsets.ModelViewSet):
    pass


def check():
    pass