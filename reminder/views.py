from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, ReminderSerializer
from .models import Reminder
from rest_framework import generics
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReminderViewSet(generics.DestroyAPIView, viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    paginate_by = 15
