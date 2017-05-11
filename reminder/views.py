from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from .forms import ReminderForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile, Reminder
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
def create(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            form = reminder_form.save(commit=False)
            user = get_object_or_404(User, username=request.user.username)
            form.user = user
            form.active = True
            form.save()
            messages.info(request, 'New Reminder Added')
        else:
            logger = logging.getLogger(__name__)
            messages.error(request, reminder_form.errors)
            logger.info(reminder_form.errors)
        return redirect('create')
    return render(request, 'add.html', {'title': 'Add New Reminder'})


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            user = get_object_or_404(User, username=request.user.username)
            profile.user = user
            profile.save()
            messages.info(request, 'Profile Updated')
        else:
            logger = logging.getLogger(__name__)
            messages.error(request, profile_form.errors)
            logger.info(profile_form.errors)
        return redirect('profile')
    else:
        user = get_object_or_404(User, username=request.user.username)
        profile = Profile.objects.get(user=user)
        return render(request, 'profile.html', {'title': 'Profile Information', 'profile': profile})


@login_required
def reminders(request):
    reminders = Reminder.objects.order_by('-id')
    paginator = Paginator(reminders, 8)
    page = request.GET.get('page')
    try:
        reminder = paginator.page(page)
    except PageNotAnInteger:
        # If yummy is not an integer, deliver first page.
        reminder = paginator.page(1)
    except EmptyPage:
        reminder = paginator.page(paginator.num_pages)
    return render(request, 'reminders.html', {"reminders": reminder, 'title': 'All Reminders'})
