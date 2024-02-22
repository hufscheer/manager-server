import boto3
from decouple import config
from abc import ABC, abstractmethod

class AbstractSqsConnect(ABC):

    @abstractmethod
    def send_message_to_sqs(self, s3_key):
        pass

class SqsConnect(AbstractSqsConnect):
    _aws_access_key = config('S3_ACCESS_KEY')
    _aws_secret_key = config('S3_SECRET_ACCESS_KEY')
    _sqs_queue_url = config('SQS_QUEUE_URL')
    
    def __init__(self):
        self._sqs_conn = boto3.client('sqs', aws_access_key_id=self._aws_access_key, aws_secret_access_key=self._aws_secret_key)

    def send_message_to_sqs(self, s3_key):
        response = self._sqs_conn.send_message(
            QueueUrl=self._sqs_queue_url,
            MessageBody=s3_key
        )
        return response

class FakeSqsConnect(AbstractSqsConnect):

    def send_message_to_sqs(self, s3_key):
        return True