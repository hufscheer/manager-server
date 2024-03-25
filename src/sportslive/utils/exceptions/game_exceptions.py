from rest_framework.exceptions import APIException

class CantDeleteGameError(APIException):
    status_code = 400
    default_detail = "현재 상태는 게임을 삭제할 수 없습니다."

class CantParsingYoutubeUrl(APIException):
    status_code = 400
    default_detail = "유튜브 링크 형식이 잘못되었습니다."
    default_code = "cant_parsing_youtube_url"

class BiggerThanMaxRoundError(APIException):
    status_code = 400
    default_detail = "리그의 최대 라운드 보다 크게 할 수 없습니다."
    default_code = "bigger_than_max_round_error"