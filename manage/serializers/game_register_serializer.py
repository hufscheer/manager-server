from rest_framework import serializers
from manage.models import Game

class GameRegisterRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('name', 'member', 'sports_name', 'first_team', 'second_team', 'start_time')