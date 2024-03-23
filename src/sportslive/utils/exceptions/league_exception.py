from rest_framework.exceptions import APIException

class CantEndAtFasterThanStartAt(APIException):
    status_code = 400
    default_detail = "종료 시각은 시작 시간보다 빠를 수 없습니다."
    default_code = 'cant_end_at_faster_than_start_at'
