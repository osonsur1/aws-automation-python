# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:331873657685:handleLabelDetectionTopic:0cbe0434-515e-45b3-8ec7-5882c648cf95', 'Sns': {'Type': 'Notification', 'MessageId': '9d33b42d-8d7a-5f18-b516-e34acaa033de', 'TopicArn': 'arn:aws:sns:us-east-1:331873657685:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"54a396a713cd48a80ec0b3eb6c3b8896a300f03cf64a17d4c2543a8f2e37cb1b","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1592608154857,"Video":{"S3ObjectName":"Pexels Horses Video.mp4","S3Bucket":"rekovideolyzervideosdev"}}', 'Timestamp': '2020-06-19T23:09:14.910Z', 'SignatureVersion': '1', 'Signature': 'FSUn7nZqYZVne/Y2c/cp3xygYa3+0W4mxH0RCg6gXKKmA1T32lrlVzREHHHiuysbgxrSRiB9ENOgAxKFcZAhOSG3mcdPyyjdcVOuCStccky2bCYUOQGwiShYGoTVX/ok//Djcfq8NyQxYa4Zohv2Mp59lbZIkk3ekLuMLeKa5DN5l0RJ5mkgVDnRSXBlkDpJEcr8fzV+NSx15LEwDxxvFy8Hb23d5Mw6CYRiQWN0E08ZhGGo5qUgV1kvYv4xIxsup/9snD5WMkQ4vkQrdHI3w9Px5392HZZBsksxu6Dft4zos9QewKyQabSs0pFotFVtVMMk3LDM8m41N39qY0GqSw==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:331873657685:handleLabelDetectionTopic:0cbe0434-515e-45b3-8ec7-5882c648cf95', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']
type(event['Records'][0]['Sns']['Message'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
