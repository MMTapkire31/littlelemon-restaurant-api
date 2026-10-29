from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Booking, MenuItem

User = get_user_model()

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "first_name", "reservation_date", "reservation_slot"]

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={"input_type": "password"})
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
