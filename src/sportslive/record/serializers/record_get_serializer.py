from rest_framework import serializers
from record.domain import ScoreRecord, ReplacementRecord, Record
from sport.serializers import SportsQuarterResponseSerializer
from game.serializers import GameTeamNameInfoSerializer, LineupPlayerNameNumberGetSerializer

class _RecordResponseSerialzier(serializers.ModelSerializer):
    gameTeam = GameTeamNameInfoSerializer(source='game_team')
    recordedQuarter = SportsQuarterResponseSerializer(source='recorded_quarter')
    recordedAt = serializers.IntegerField(source='recorded_at')
    recordType = serializers.CharField(source='record_type')

    class Meta:
        model = Record
        fields = ('game', 'gameTeam', 'recordedQuarter', 'recordedAt', 'recordType')

class ScoreRecordResponseSerializer(serializers.ModelSerializer):
    recordInfo = _RecordResponseSerialzier(source='record')
    lineupPlayer = LineupPlayerNameNumberGetSerializer(source='lineup_player')

    class Meta:
        model = ScoreRecord
        fields = ('recordInfo', 'lineupPlayer', 'score')

class ReplacementRecordResponseSerializer(serializers.ModelSerializer):
    recordInfo = _RecordResponseSerialzier(source='record')
    originLineupPlayer = LineupPlayerNameNumberGetSerializer(source='origin_lineup_player')
    replacedLineupPlayer = LineupPlayerNameNumberGetSerializer(source='replaced_lineup_player')

    class Meta:
        model = ReplacementRecord
        fields = ('recordInfo', 'originLineupPlayer', 'replacedLineupPlayer')