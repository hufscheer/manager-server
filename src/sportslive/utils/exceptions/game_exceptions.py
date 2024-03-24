from rest_framework.exceptions import APIException

class CantDeleteGameError(APIException):
    status_code = 400
    default_detail = "현재 상태는 게임을 삭제할 수 없습니다."

class CantParsingYoutubeUrl(APIException):
    status_code = 400
    default_detail = "유튜브 링크 형식이 잘못되었습니다."