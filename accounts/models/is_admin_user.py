from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        is_administrator = bool(int.from_bytes(request.user.is_administrator, byteorder='big'))
        return bool(request.user and is_administrator)
 