import requests
import django
import os
import logging


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()


def mail()