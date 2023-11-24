from rest_framework import serializers
from game.domain import GameTeam
from report.domain import Comment, Report

class GameInfoSerializer(serializers.ModelSerializer):
    leagueName = serializers.CharField(source='game.league.name')
    sportName = serializers.CharField(source='game.sport.name')
    gameName = serializers.CharField(source='game.name')

    class Meta:
        model = GameTeam
        fields = ('leagueName', 'sportName', 'gameName',)

class CommentInfoSerializer(serializers.ModelSerializer):
    commentId = serializers.IntegerField(source='id')
    createdAt = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Comment
        fields = ('commentId', 'content', 'createdAt',)

class CommentReportInfoSerializer(serializers.ModelSerializer):
    commentId = serializers.IntegerField(source='comment.id')
    reportId = serializers.IntegerField(source='id')
    content = serializers.CharField(source='comment.content')
    createdAt = serializers.DateTimeField(source='comment.created_at')
    reportedAt = serializers.DateTimeField(source='reported_at')

    class Meta:
        model = Report
        fields = ('commentId', 'reportId', 'content', 'createdAt', 'reportedAt',)

class PendingReportSerializer(serializers.Serializer):
    gameInfo = GameInfoSerializer(source='game_info')
    reportInfo = CommentReportInfoSerializer(source='report_info')
    
class IsBlockedReportSerializer(serializers.Serializer):
    gameInfo = GameInfoSerializer(source='game_info')
    reportInfo = CommentInfoSerializer(source='report_info')

class ReportResponseSerializer(serializers.Serializer):
    pending = PendingReportSerializer(many=True)
    isBlocked = IsBlockedReportSerializer(many=True, source='is_blocked_comments')
