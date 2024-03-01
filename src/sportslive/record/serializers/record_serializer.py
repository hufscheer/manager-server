from rest_framework import serializers

class ScoreRecordRequestSerializer(serializers.Serializer):
    gameTeamId = serializers.IntegerField(source='game_team_id')
    recordedQuarterId = serializers.IntegerField(source='recorded_quarter_id')
    scoreLineupPlayerId = serializers.IntegerField(source='score_lineup_player_id')
    score = serializers.IntegerField()

class ReplacementRecordRequestSerializer(serializers.Serializer):
    gameTeamId = serializers.IntegerField(source='game_team_id')
    recordedQuarterId = serializers.IntegerField(source='recorded_quarter_id')
    originLineupPlayerId = serializers.IntegerField(source='origin_lineup_player_id')
    replacedLineupPlayerId = serializers.IntegerField(source='replaced_lineup_player_id')