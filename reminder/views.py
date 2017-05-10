from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from .forms import ReminderForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import logging


def index(request):
    if request.user.is_authenticated:
        return redirect('create')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('create')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect('/')
    else:
        return render(request, 'login.html')


@login_required
def add(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            form = reminder_form.save(commit=False)
            user = User.objects.get(username=request.user.username)
            form.user = user
            form.save()
            messages.info(request, 'New Reminder Added')
        else:
            logger = logging.getLogger(__name__)
            messages.error(request, reminder_form.errors)
            logger.info(reminder_form.errors)
        return redirect('create')
    return render(request, 'add.html', {'title': 'Add New Reminder'})
