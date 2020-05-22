import uuid

import boto3
from botocore.exceptions import ClientError
import json

print('Loading function')

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.eu-west-1.amazonaws.com/620996823437/CCBDAProject-Queue.fifo'

sender_email = 'marvidalsegura@gmail.com'


def send_email(email, simulation_id):
    SENDER = "Sender Name <{}>".format(sender_email)
    RECIPIENT = email

    AWS_REGION = "eu-west-1"

    # The subject line for the email.
    SUBJECT = "Infection Simulator Confirmation"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Infection Simulator Confirmation\r\n"
                 "Your simulation has started! "
                 "Soon you will receive an email with the results."
                 "This is your simulation id: {}"
                 ).format(simulation_id)

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Infection Simulator Confirmation</h1>
      <p>Your simulation has started! Soon you will receive an email with the results.</p>
      <p>This is your simulation id: {}</p>
    </body>
    </html>
                """.format(simulation_id)

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def respond(err, res=None):
    if not err:
        print('Message Added in the Queue')

    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps(str(err) if err else res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }


def lambda_handler(event, context):
    operation = event['requestContext']['http']['method']
    if operation == 'POST':
        body = event['body']
        body_dict = json.loads(body)
        user_email = body_dict['initial_data'].pop('user_email')
        body = json.dumps(body_dict)
        simulation_id = str(uuid.uuid4())
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageAttributes={
                'Simulation_id': {
                    'StringValue': simulation_id,
                    'DataType': 'String'
                },
                'User_email': {
                    'StringValue': user_email,
                    'DataType': 'String'
                }
            },
            MessageGroupId='Initial_data',
            MessageDeduplicationId=simulation_id,
            MessageBody=body
        )
        send_email(user_email, simulation_id)
        return respond(None, response)
    else:
        return respond(ValueError('Unsupported method {}'.format(operation)))
