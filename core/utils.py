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




