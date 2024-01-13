import os
from celery import Celery
from django.conf import settings  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LabelWebApp.settings')
  
app = Celery('LabelWebApp')
  
# app.config_from_object('LabelWebApp.celeryconfig')
app.config_from_object('django.conf:settings',namespace='CELERY')
  

app.autodiscover_tasks()

app.conf.update(
    worker_max_tasks_per_child=1,
    broker_pool_limit=None
)

app.conf.task_default_queue = settings.TASK_QUEUE_NAME
app.conf.task_default_exchange = settings.TASK_QUEUE_NAME
app.conf.task_default_routing_key = settings.TASK_QUEUE_NAME


# print("Broker URL issss:", app.conf.broker_url)