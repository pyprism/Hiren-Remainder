from twilio.rest import Client
import django
import os
import logging


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()


def sms(sid, token, to, from_, body):
    try:
        client = Client(sid, token)
        client.messages.create(
            to=to,
            from_=from_,
            body=body
        )
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(e)
