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

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
