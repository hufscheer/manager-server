from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.domain import IsAdminUser
from league.containers import LeagueContainer

class LeagueView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._league_serivice = LeagueContainer.league_service()

    def post(self, request):
        self._league_serivice.register_league(request.data, request.user)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
            self._league_serivice.change_league(request.data, request.user)
            return Response(status.HTTP_200_OK)
        except League.DoesNotExist:
            return Response({"error": "리그를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request):
        try:
            self._league_serivice.delete_league(request.data, request.user)
            return Response(status.HTTP_204_NO_CONTENT)
        except League.DoesNotExist:
            return Response({"error": "리그를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
