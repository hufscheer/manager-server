from rest_framework import serializers
from game.domain import GameTeam, LineupPlayer

class GameTeamSaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeam
        fields = '__all__'

class GameTeamRequestSerializer(serializers.Serializer):
    teamIds = serializers.ListField(child=serializers.IntegerField(), source='team_ids')

class LineupPlayerRequestSerialzier(serializers.ModelSerializer):
    isCaptain = serializers.BooleanField(source='is_captain')

    class Meta:
        model = LineupPlayer
        fields = ('name', 'description', 'number', 'isCaptain')

class LineupPlayerSaveSerialzier(serializers.ModelSerializer):

    class Meta:
        model = LineupPlayer
        fields = '__all__'

class LineupPlayerChangeSerialzier(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    isCaptain = serializers.BooleanField(source='is_captain')
    
    class Meta:
        model = LineupPlayer
        fields = ('id', 'name', 'description', 'number', 'isCaptain')

class _GameTeamScoreMappingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    score = serializers.IntegerField()

class GameScoreChangeSerializer(serializers.Serializer):
    teamIdScore = _GameTeamScoreMappingSerializer(many=True, source='team_score')