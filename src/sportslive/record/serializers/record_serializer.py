from rest_framework import serializers

class ScoreRecordRequestSerializer(serializers.Serializer):
    recordedAt = serializers.DateTimeField(source='recorded_at')
    gameTeamId = serializers.IntegerField(source='game_team_id')
    scoreLineupPlayerId = serializers.IntegerField(source='score_lineup_player_id')
    recordedQuarterId = serializers.IntegerField(source='recorded_quarter_id')
    score = serializers.IntegerField()

class ReplacementRecordRequestSerializer(serializers.Serializer):
    recordedAt = serializers.DateTimeField(source='recorded_at')
    gameTeamId = serializers.IntegerField(source='game_team_id')
    recordedQuarterId = serializers.IntegerField(source='recorded_quarter_id')
    originLineupPlayerId = serializers.IntegerField(source='origin_lineup_player_id')
    replacedLineupPlayerId = serializers.IntegerField(source='replaced_lineup_player_id')

class ScoreRecordChangeRequestSerializer(serializers.Serializer):
    recordedAt = serializers.IntegerField(source='recorded_at')
    gameTeamId = serializers.IntegerField(source='game_team_id')
    recordedQuarterId = serializers.IntegerField(source='recorded_quarter_id')
    scoreLineupPlayerId = serializers.IntegerField(source='score_lineup_player_id')
    score = serializers.IntegerField()

class ReplacementRecordChangeRequestSerializer(serializers.Serializer):
    recordedAt = serializers.IntegerField(source='recorded_at')
    gameTeamId = serializers.IntegerField(source='game_team_id')
    recordedQuarterId = serializers.IntegerField(source='recorded_quarter_id')
    originLineupPlayerId = serializers.IntegerField(source='origin_lineup_player_id')
    replacedLineupPlayerId = serializers.IntegerField(source='replaced_lineup_player_id')