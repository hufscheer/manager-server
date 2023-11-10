from decouple import config
import boto3
from rest_framework import exceptions
import uuid

def upload_to_s3(image_data, team_name: dict, league_name: str):
    aws_access_key = config('S3_ACCESS_KEY')
    aws_secret_key = config('S3_SECRET_ACCESS_KEY')
    bucket_name = config('BUCKET_NAME')
    team_name = team_name.get('name')
    try:
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        object_name = f"{team_name}.{image_data.content_type}"
        key = league_name + '/' + object_name
        s3.put_object(Body=image_data, Bucket=bucket_name, Key=key, ContentType='jpg')
        url = f"https://{bucket_name}.s3.ap-northeast-2.amazonaws.com/{key}"
        return url
    
    except Exception as e:
        raise exceptions.ValidationError(f"s3 업로드에 에러가 발생했습니다.: {str(e)}")