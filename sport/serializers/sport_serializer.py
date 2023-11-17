from rest_framework import serializers
from sport.domain import Sport, Quarter

class SportsNameResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sport
        fields = ('name',)

class SportsQuarterResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quarter
        fields = ('name',)