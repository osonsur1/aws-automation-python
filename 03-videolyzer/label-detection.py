# coding: utf-8
import boto3
from pathlib import Path

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

rekognition_client = session.client('rekognition')

bucket = s3.create_bucket(Bucket='rekovideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})

pathname = '~/Downloads/video.mp4'
path = Path(pathname).expanduser().resolve()
print(path)

bucket.upload_file(str(path), str(path.name))

response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})

job_id = response['JobId']

result = rekognition_client.get_label_detection(JobId=job_id)

result.keys()

result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']

len(result['Labels'])
