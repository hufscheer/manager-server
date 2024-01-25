from rest_framework import serializers
from game.domain import GameTeam
from report.domain import CheerTalk, Report

class _GameInfoSerializer(serializers.ModelSerializer):
    leagueName = serializers.CharField(source='game.league.name')
    sportName = serializers.CharField(source='game.sport.name')
    gameName = serializers.CharField(source='game.name')

    class Meta:
        model = GameTeam
        fields = ('leagueName', 'sportName', 'gameName',)

class _CheerTalkInfoSerializer(serializers.ModelSerializer):
    cheerTalkId = serializers.IntegerField(source='id')
    createdAt = serializers.DateTimeField(source='created_at')

    class Meta:
        model = CheerTalk
        fields = ('cheerTalkId', 'content', 'createdAt',)

class _CheerTalkReportInfoSerializer(serializers.ModelSerializer):
    cheerTalkId = serializers.IntegerField(source='cheer_talk.id')
    reportId = serializers.IntegerField(source='id')
    content = serializers.CharField(source='cheer_talk.content')
    createdAt = serializers.DateTimeField(source='cheer_talk.created_at')
    reportedAt = serializers.DateTimeField(source='reported_at')

    class Meta:
        model = Report
        fields = ('cheerTalkId', 'reportId', 'content', 'createdAt', 'reportedAt',)

class _PendingReportSerializer(serializers.Serializer):
    gameInfo = _GameInfoSerializer(source='game_info')
    reportInfo = _CheerTalkReportInfoSerializer(source='report_or_cheer_talk')
    
class _IsBlockedReportSerializer(serializers.Serializer):
    gameInfo = _GameInfoSerializer(source='game_info')
    reportInfo = _CheerTalkInfoSerializer(source='report_or_cheer_talk')

class ReportResponseSerializer(serializers.Serializer):
    pending = _PendingReportSerializer(many=True)
    isBlocked = _IsBlockedReportSerializer(many=True, source='blocked_cheer_talks_infos')
