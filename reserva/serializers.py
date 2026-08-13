from rest_framework import serializers
from .models import Shows, Reservations

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ["id", "movie_title", "room", "price"]

class ReservationSerializer(serializers.ModelSerializer):
    shows = serializers.CharField(source="show.movie_title", read_only=True)

    class Meta:
        model = Reservations
        fields = ["id", "show_id", "customer_name ", "seats", "status", "created_at"]