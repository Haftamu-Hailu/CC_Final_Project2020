import boto3
import time
import json
import os

sqs = boto3.client('sqs',region_name='eu-west-2',
                    aws_access_key_id=os.environ['access_id'],
                    aws_secret_access_key=os.environ['access_key'])


queue_url_receive = 'https://sqs.eu-west-2.amazonaws.com/459864568246/conf_queue'
queue_url_send = 'https://sqs.eu-west-2.amazonaws.com/459864568246/sim_test'



def send_message(message, queue_url):
    print('Message sent')
    sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=0,
    MessageBody= message
    )
    return "sent message"

def receive_message(queue_url,nr_msg):
    print('Message received')
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=nr_msg,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=30,
        WaitTimeSeconds=0
        )
    return response

def delete_message(message,queue_url):
    try:
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=receipt_handle
                )
    except KeyError as e:
                print(repr(e))
                print("No Message to delete.")