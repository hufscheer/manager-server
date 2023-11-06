from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    message = "관리자 권한이 필요합니다."
    
    def has_permission(self, request, view):
        is_administrator = bool(int.from_bytes(request.user.is_administrator, byteorder='big'))
        return bool(request.user and is_administrator)
 