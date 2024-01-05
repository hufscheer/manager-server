from rest_framework.views import exception_handler
from utils.exceptions.team_exceptions import S3UploadError, TeamSaveError

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, (S3UploadError, TeamSaveError)):
            response.data['teamName'] = exc.team_name

    return response
