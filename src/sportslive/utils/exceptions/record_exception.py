from rest_framework.exceptions import APIException

class NotValidRecordTypeError(APIException):
    status_code = 400
    default_detail = "유효하지 않은 레코드 타입"
