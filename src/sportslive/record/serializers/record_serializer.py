from rest_framework import serializers
from record.domain import Record

class RecordRequestSerializer(serializers.ModelSerializer):
    gameTeamId = serializers.IntegerField(source='game_team_id')
    lineupPlayerId = serializers.IntegerField(source='lineup_player_id')
    score = serializers.IntegerField()
    quarterId = serializers.IntegerField(source='quarter_id')

    class Meta:
        model = Record
        fields = ('gameTeamId', 'lineupPlayerId', 'score', 'quarterId')