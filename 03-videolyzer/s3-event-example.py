# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2020-06-19T20:39:09.188Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAU2RJWENKUTOXN746Q'}, 'requestParameters': {'sourceIPAddress': '108.28.56.237'}, 'responseElements': {'x-amz-request-id': 'BBD38F809E1D51DA', 'x-amz-id-2': '4SyxRtpPn6OmZlq7m9BU40PckL+CvFrV3gqVq/Ycto2E5yPtc/JyHQvQdb+BMAU5FiakVrX36KhlpAXoN65P28/L32eD7dVJ'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'b4a0177a-5d68-4e9b-9c5c-ee1f2d636df8', 'bucket': {'name': 'rekovideolyzervideosdev', 'ownerIdentity': {'principalId': 'A2QSR246VCEF5'}, 'arn': 'arn:aws:s3:::rekovideolyzervideosdev'}, 'object': {'key': 'Pexels+Horses+Video.mp4', 'size': 59408944, 'eTag': '365ca66d4ace957ef186f8e9e08e8c36-8', 'sequencer': '005EED226B6879641D'}}}]}
event
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
