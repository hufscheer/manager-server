from django.urls import path, include
from .views import (
                GameTeamListView,
                GameStatusChangeView,
                GameRegisterView,
                GameScoreChangeView,
            )
from .views.comment_block_view import CommentBlockView
app_name = 'manage'

urlpatterns = [
    path('game/register/', GameRegisterView.as_view(), name='GameRegisterView'),
    path('game/score/<int:game_id>/', GameScoreChangeView.as_view(), name='GameScoreChangeView'),
    path('game/teamlist/<int:game_id>/', GameTeamListView.as_view(), name='GameTeamListView'),
    path('game/statustype/<int:game_id>/', GameStatusChangeView.as_view(), name='GameStatusChangeView'),
    path('comments/block/<int:comment_id>/', CommentBlockView.as_view(), name='CommentBlockView'),
]