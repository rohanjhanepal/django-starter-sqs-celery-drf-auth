from random import choice
import os
from django.conf import settings
import json
import random
import boto3


def choose_random_from_list(elements):
    try:
        """
        picks randomly
        """
        element = random.choice(elements)
        while element.keep == True:
            element = random.choice(elements)
        return element
    except:
        return None

def get_directories():
    dirs = list()
    s3 = settings.S3_CLIENT
    result = s3.list_objects_v2(Bucket= settings.S3_DATA_BUCKET, Delimiter='/')
    for prefix in result.get('CommonPrefixes', []):
        dirs.append(prefix['Prefix'][:-1])

    return dirs

def get_files_in_directories(directory):
    dirs = list()
    s3 = settings.S3_CLIENT
    result = s3.list_objects_v2(Bucket= settings.S3_DATA_BUCKET, Prefix=f'{directory}/',Delimiter='/')
    for content in result.get('Contents', [])[1:]:
        dirs.append(content['Key'])
    return dirs
    
       
def generate_presigned_url(object_key, expiration=3600):
    s3 = settings.S3_CLIENT
    try:
        url = s3.generate_presigned_url('get_object',
                                        Params={'Bucket': settings.S3_DATA_BUCKET, 'Key': object_key},
                                        ExpiresIn=expiration)
    except Exception as e:
        # print(f"An error occurred: {e}")
        return None

    return url

def get_cloudfront_url(object_key):
    return f"{settings.CLOUD_FRONT_DISTRIBUTION_URL}{object_key}"

def getObjectClassesS3():
   
    lists = get_directories()
    choosen = choice(lists)

    lists = get_files_in_directories(choosen)
    choosen_image = choice(lists)
    
    return (choosen , choosen_image)

def getNepaliDigits():
    CHARACTERS = ['yna', 'taamatar', 'thaa', 'daa', 'dhaa', 'adna', 'tabala', 'tha', 'da', 'dha', 'ka', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'yaw', 'ra', 'la', 'waw', 'kha', 'motosaw', 'petchiryakha', 'patalosaw', 'ha', 'chhya', 'tra', 'gya', 'ga', 'gha', 'kna', 'cha', 'chha', 'ja', 'jha']
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    path = os.path.join(settings.BASE_DIR , settings.PUZZLE_FOLDER , settings.NEPALI_HANDWRITTEN_FOLDER)
    lists = os.listdir(path)
    choosen = choice(lists)
    if 'character' in choosen:
        letter_data = choosen.split('_')[2]
    if 'digit' in choosen:
        letter_data = choosen.split('_')[1]

    lists = os.listdir(os.path.join(settings.BASE_DIR , settings.PUZZLE_FOLDER , settings.NEPALI_HANDWRITTEN_FOLDER ,choosen ))
    choosen_image = choice(lists)
    user_choices = list()
    for i in range(0,4):
        ch = choice(CHARACTERS)
        if ch not in user_choices:
            user_choices.append(ch)
            continue
        ch = choice(CHARACTERS)
        user_choices.append(ch)

    if letter_data not in user_choices: #REMOVE AFTER ADDING UNLABBELED DATA
        user_choices.append(letter_data)

    url = f"/{settings.MEDIA}/{settings.SOLVE}/{settings.NEPALI_HANDWRITTEN_FOLDER}/{choosen}/{choosen_image}"
    return (user_choices , url)

def getObjectClasses():
    path = os.path.join(settings.BASE_DIR , settings.PUZZLE_FOLDER , settings.OBJECT_CLASSES_FOLDER)
    lists = os.listdir(path)
    choosen = choice(lists)

    lists = os.listdir(os.path.join(settings.BASE_DIR , settings.PUZZLE_FOLDER , settings.OBJECT_CLASSES_FOLDER ,choosen ))
    choosen_image = choice(lists)
    user_choices = list()
    for i in range(0,4):
        ch = choice(lists)
        if ch not in user_choices:
            user_choices.append(ch)
            continue
        ch = choice(lists)
        user_choices.append(ch)
    url = f"/{settings.MEDIA}/{settings.SOLVE}/{settings.OBJECT_CLASSES_FOLDER}/{choosen}/{choosen_image}"
    
    return (choosen , url)

# url = s3.generate_presigned_url('get_object',
#                                        Params={'Bucket': 'labelappdata', 'Key': 'dog/1.jpg','ResponseContentDisposition': 'attachment'},
#                                        ExpiresIn=3600)

def get_ticket_number():
    return ''.join(random.choices('0123456789abcdef', k=8))


def get_length_of_queue():

    response = settings.SQS_CLIENT.get_queue_attributes(
        QueueUrl=settings.DATA_QUEUE_URL,
        AttributeNames=['ApproximateNumberOfMessages']
        )
    message_count = int(response['Attributes']['ApproximateNumberOfMessages'])

    return message_count

def push_to_queue(data):
    
    message_body = json.dumps(data)
    response = settings.SQS_CLIENT.send_message(
        QueueUrl=settings.DATA_QUEUE_URL,
        MessageBody=message_body,
        MessageGroupId= settings.MESSAGE_GROUP_ID
    )
     

    # response = sqs_client.send_message(
    #     QueueUrl=DATA_QUEUE_URL,
    #     MessageBody='one'
    # )
    # response = sqs_client.receive_message(
    #     QueueUrl=DATA_QUEUE_URL,
    #     MaxNumberOfMessages=1,
    # )
    # response = sqs_client.get_queue_attributes(
    #     QueueUrl=DATA_QUEUE_URL,
    #     AttributeNames=['ApproximateNumberOfMessages']
    #     )
    return True

def pop_from_queue():
    
    response = settings.SQS_CLIENT.receive_message(
        QueueUrl=settings.DATA_QUEUE_URL,
        MaxNumberOfMessages=1,
    )

    messages = response.get('Messages')
    if messages:
        message = messages[0]
        body = json.loads(message['Body'])
        settings.SQS_CLIENT.delete_message(
            QueueUrl=settings.DATA_QUEUE_URL,
            ReceiptHandle=message['ReceiptHandle']
        )
        return body
    
    return None
    
