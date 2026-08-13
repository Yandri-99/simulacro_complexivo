from rest_framework import serializers

class MovieCatalogSerializer(serializers.Serializer):
    movie_title = serializers.CharField(max_length=120)
    genre = serializers.CharField(max_length=120)
    rating = serializers.CharField(max_length=120)
    duration_min = serializers.FloatField(required=False)
    is_active = serializers.BooleanField(default=True)

class EventType:
        CREATED = "CREATED"
        CONFIRMED = "CONFIRMED"
        CANCELLED = "CANCELLED"
        CHECKED_IN = "CHECKED_IN"

        CHOICES = [
            (CREATED, "CREATED"),
            (CONFIRMED, "CONFIRMED"),
            (CANCELLED, "CANCELLED"),
            (CHECKED_IN, "CHECKED_IN"),
        ]

class Source:
        WEB = "WEB"
        MOBILE = "MOBILE"
        SYSTEM = "SYSTEM"

        CHOICES = [
            (WEB, "WEB"),
            (MOBILE, "MOBILE"),
            (SYSTEM, "SYSTEM"),
        ]

    

class ReservationEventsSerializer(serializers.Serializer):
    reservation_id = serializers.IntegerField()        # ID de Vehiculo (Postgres)
    eventType = serializers.ChoiceField(choices=EventType.CHOICES,default=EventType.CREATED)       # ObjectId (string) de service_types
    source = serializers.ChoiceField(choices=Source.CHOICES,default=Source.WEB)
    notes = serializers.CharField(required=False, allow_blank=True)
    created_at = serializers.DateField(required=False)
    