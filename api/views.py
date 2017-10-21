from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from reminder.models import Reminder
from .serializers import ReminderSerializer


@csrf_exempt
def login(request):
    """
    token authentication for api
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': str(token[0])})
        else:
            return JsonResponse({'error': 'Username/Password is not valid'})


class ReminderViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


