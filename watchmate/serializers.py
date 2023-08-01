from rest_framework import serializers

from .models import *

class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model= Watchlist
        exclude =('active',)

    
class ReviewSerializer(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model= Review
        exclude =('watchlist',)

    