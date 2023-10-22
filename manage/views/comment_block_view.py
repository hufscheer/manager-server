from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models.is_admin_user import IsAdminUser
from manage.containers import ManageContainer

class CommentBlockView(APIView):
    """
    댓글을 검열하는 view
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._comment_block_service = ManageContainer.comment_block_service()

    def post(self, request, comment_id: int):
        try:
            self._comment_block_service.block_comment(comment_id)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
             return Response({"detail": "잘못된 요청입니다.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
