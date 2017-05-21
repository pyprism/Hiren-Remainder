from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from .forms import ReminderForm, ProfileForm
from django.shortcuts import get_object_or_404
from .models import Profile, Reminder
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging


def index(request):
    """
    Handle authentication
    :param request: 
    :return: 
    """
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
            troll = "Username/Password is not valid! And your password must include " \
                    "a gang sign,a haiku and the blood of a virgin"  # :D  :D  lol
            messages.error(request, troll)
            return redirect('/')
    else:
        return render(request, 'login.html')


@login_required
def create(request):
    """
    Create new reminder
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            form = reminder_form.save(commit=False)
            form.user = request.user
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
    """
    Save API information
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.info(request, 'Profile Updated')
        else:
            logger = logging.getLogger(__name__)
            messages.error(request, profile_form.errors)
            logger.info(profile_form.errors)
        return redirect('profile')
    else:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile.html', {'title': 'Profile Information', 'profile': profile})


@login_required
def reminders(request):
    """
    Serve all reminders
    :param request: 
    :return: 
    """
    reminders = Reminder.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(reminders, 8)
    page = request.GET.get('page')
    try:
        reminder = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reminder = paginator.page(1)
    except EmptyPage:
        reminder = paginator.page(paginator.num_pages)
    return render(request, 'reminders.html', {"reminders": reminder, 'title': 'All Reminders'})


@login_required
def reminder(request, pk=None):
    """
    Serve single reminder
    :param request: 
    :param pk: 
    :return: 
    """
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
    return render(request, 'reminder.html', {'reminder': reminder, 'title': 'Reminder'})


@login_required
def reminder_update(request, pk=None):
    """
    Handle reminder update
    :param request: 
    :param pk: 
    :return: 
    """
    if request.method == 'POST':
        reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
        reminder_form = ReminderForm(request.POST, instance=reminder)
        if reminder_form.is_valid():
            reminder_form.save()
            messages.info(request, 'Reminder Updated')
        else:
            logger = logging.getLogger(__name__)
            messages.error(request, reminder_form.errors)
            logger.info(reminder_form.errors)
        return redirect('/reminder/' + pk + '/update/')
    else:
        reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
        return render(request, 'reminder_update.html', {'reminder': reminder, 'title': 'Update Reminder'})
