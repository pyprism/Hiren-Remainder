from __future__ import absolute_import
__author__ = 'prism'

# from celery.task.base import periodic_task
# from django.utils.timezone import timedelta


# @periodic_task(run_every=timedelta(seconds=5))
# from celery import Celery
# from celery import shared_task
#
# app = Celery('tasks')
#
# @app.task
# def run():
#     print('Nisha')

from hiren.celery_app import app
from celery import shared_task

#app = Celery('tasks', broker='redis://localhost')

@app.task()
def runs():
    print('hello')

