from rest_framework import serializers
from sport.domain import Sport, Quarter

class SportsNameResponseSerializer(serializers.ModelSerializer):
    sportId = serializers.CharField(source='id')

    class Meta:
        model = Sport
        fields = ('sportId', 'name',)

class SportsQuarterResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quarter
        fields = ('name',)