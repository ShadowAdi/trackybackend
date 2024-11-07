from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    def validate(self, data):
        print("Incoming data for validation:", data)  # Log incoming data
        return data
    
    # Define optional fields explicitly
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    github_url = serializers.URLField(required=False, allow_blank=True)
    linked_in_url = serializers.URLField(required=False, allow_blank=True)
    photo = serializers.URLField(required=False, allow_blank=True)
    resume = serializers.URLField(required=False, allow_blank=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "username",
            "date_joined",
            "first_name",
            "last_name",
            "github_url",
            "linked_in_url",
            "photo",
            "resume",
        ]
