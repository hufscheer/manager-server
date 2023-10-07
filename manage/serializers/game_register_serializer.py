from rest_framework import serializers
from manage.models import Game, Team

class GameRegisterRequestSerializer(serializers.ModelSerializer):
    sportsName = serializers.CharField(source='sports_name')
    firstTeam = serializers.PrimaryKeyRelatedField(source='first_team', queryset=Team.objects.all())
    secondTeam = serializers.PrimaryKeyRelatedField(source='second_team', queryset=Team.objects.all())
    startTime = serializers.DateTimeField(source='start_time')

    class Meta:
        model = Game
        fields = ('name', 'member', 'sportsName', 'firstTeam', 'secondTeam', 'startTime')