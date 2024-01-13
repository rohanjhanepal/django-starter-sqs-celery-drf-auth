from celery import shared_task , chain
from celery.signals import task_success
from LabelWebApp.celery import app
from django.conf import settings





