import requests
import django
import os
import logging


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()


def mail(url, key, sender, recipient, title, message):
    """
    Mailgun sender
    :param url: mailgun api url
    :param key: mailgun api key
    :param sender: sender email
    :param recipient: recipient email
    :param title: email title
    :param message: email body
    :return:
    """
    logger = logging.getLogger(__name__)
    try:
        requests.post(url + '/messages', auth=('api', key),
                      data={
                          "from": "New Reminder <" + sender + ">",
                          "to": [recipient],
                          "subject": "Reminder about: " + title,
                          "text": message
                      })
    except Exception as e:
        logger.error(e)
