from kombu.utils.url import as_url

 
BROKER_URL = as_url(
    scheme="sqs",
    hostname='sqs.us-east-1.amazonaws.com',   
    access_key=None,  
    secret_key=None,   
    path="/426857564226/LabelAppQueueCelery"
)

 
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

 
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-east-1',  
    'visibility_timeout': 3600,   
    'polling_interval': 5,   
}
