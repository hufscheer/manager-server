from rest_framework import serializers
from manage.models import Team, Game

class TeamDetailSerializer(serializers.ModelSerializer):
    logoImageUrl = serializers.CharField(source='logo_image_url')

    class Meta:
        model = Team
        fields = ('id', 'name', 'logoImageUrl')

class GameListSerializer(serializers.ModelSerializer):
    firstTeam = TeamDetailSerializer(source='first_team', read_only=True)
    secondTeam = TeamDetailSerializer(source='second_team', read_only=True)

    class Meta:
            model = Game
            fields = ('firstTeam', 'secondTeam')