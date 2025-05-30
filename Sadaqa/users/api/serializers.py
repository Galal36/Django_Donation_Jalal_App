from rest_framework import serializers
from ..models import CustomUser


# Convert CustomUser model objects into JSON format (for APIs).
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone",
            "birthdate",
            "pic",
            "country",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_phone(self, value):
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError(
                "This phone number is already registered."
            )
        return value


# This is used to handle user registration (signing up).
class CustomUserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    birthdate = serializers.DateField()
    country = serializers.CharField()

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Passwords don't match")
        return data
