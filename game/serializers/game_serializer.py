from rest_framework import serializers
from game.domain import Game
from league.domain import League

class GameRequestSerializer(serializers.ModelSerializer):
    sportsId = serializers.IntegerField(source='sport')
    startTime = serializers.DateTimeField(source='start_time')
    videoId = serializers.CharField(allow_null=True, required=False, source='video_id')

    class Meta:
        model = Game
        fields = ('sportsId', 'startTime', 'name', 'videoId',)

class GameSaveSerializer(serializers.ModelSerializer):
    video_id = serializers.CharField(allow_null=True, required=False)
    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all())
    
    class Meta:
        model = Game
        fields = '__all__'