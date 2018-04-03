# -*- coding: UTF-8 -*-  

import boto3
import botocore

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
#     for object in bucket.objects.all():
#         print(object.key)

BUCKET_NAME = 'burningluffys3' # replace with your bucket name
KEY = 'AA/icon.jpg' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'AA.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise